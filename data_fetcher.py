from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from io import BytesIO
import time
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs


HOST_NAME = ''  # localhost
PORT_NUMBER = 8000
MINISTERO_SALUTE_ENCYCLOPEDIA = "http://www.salute.gov.it/portale/salute/p1_3.jsp?lingua=italiano&tema=Salute_A_Z"


class DataFetcher():
    def __init__(self, query):
        super().__init__()
        self.query = query
        self.driver = webdriver.Firefox()
        self.driver.get(MINISTERO_SALUTE_ENCYCLOPEDIA)
        # The next script is used to accept the cookie policy
        self.driver.execute_script("setPrivacy();")

    def get_query(self):
        # This instruction looks for a link in the page containing the query. The translation is needed for case insensitivity.
        found_results = []
        query_terms = []
        query_terms.append(self.query)
        for term in query_terms:
            found_results.append(self.driver.find_element_by_xpath(
                "*//a[contains(translate(@title, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), '"+term+"')]"))
        if len(found_results) == 0:
            return None
        # I could implement a "multiple results" condition too.
        else:
            found_results[0].click()
            tabs = self.driver.find_element_by_class_name("nav-tabs")
            children = tabs.find_elements_by_tag_name("li")
            informations = {}
            i = 1
            for information_tab in children:
                link = information_tab.find_element_by_tag_name("a")
                information_tab.click()
                text = ""
                tab_content = self.driver.find_element_by_id("tab-"+str(i))
                for paragraph in tab_content.find_elements_by_tag_name("p"):
                    text = text + paragraph.text
                informations[link.get_attribute(
                    "title")] = text
                i = i + 1
            return informations


class APIManager(BaseHTTPRequestHandler):
    def do_GET(self):
        parameters = parse_qs(urlparse(self.path).query)
        response = DataFetcher(parameters["query"][0])
        if response is not None:
            self.send_response(200)
        else:
            self.send_response(404)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        if response is not None:
            self.wfile.write(json.dumps(response.get_query()).encode())


def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()


if __name__ == '__main__':
    server_class = HTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), APIManager)
    print(time.asctime(), "Server Starts - %s:%s" % (HOST_NAME, PORT_NUMBER))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print('KeyboardInterrupt received.')
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (HOST_NAME, PORT_NUMBER))
