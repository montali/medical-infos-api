# Selenium scraper for the Ministero della Salute encyclopedia

This is an API that scrapes the Ministero della Salute medical encyclopedia in order to provide useful informations to the [hospital triage Mycroft skill](https://simone.codes/hospital-triage-skill). It supports GET requests only, built like this:

```
http://127.0.0.1:8000/?query=[query text]
```

The responses are JSON-formatted, and composed of the various tabs you can find on the website.

## Examples

If you want to know things about "Ictus", GET

```
http://127.0.0.1:8000/?query=ictus
```

to receive:

```json
{
  "Descrizione": "Ictus è un termine latino che significa “colpo” (in inglese stroke). Insorge, infatti, in maniera improvvisa: una persona in pieno benessere può accusare sintomi tipici che possono essere transitori, restare costanti o peggiorare nelle ore successive.Quando si verifica un’interruzione dell’apporto di sangue ossigenato in un’area del cervello, si determina la morte delle cellule cerebrali di quell’area. Di conseguenza, le funzioni cerebrali controllate da quell’area (che possono riguardare il movimento di un braccio o di una gamba, il linguaggio, la vista, l’udito o altro) vengono perse.In Italia l’ictus è la terza causa di morte, dopo le malattie ischemiche del cuore e le neoplasie; causa il 10-12% di tutti i decessi per anno e rappresenta la prima causa di invalidità. Ogni anno si verificano in Italia circa 196.000 ictus, di cui il 20% sono recidive.  Il 10-20% delle persone colpite da ictus cerebrale muore entro un mese e un altro 10% entro il primo anno di vita. Solo il 25% dei pazienti sopravvissuti ad un ictus guarisce completamente, il 75% sopravvive con una qualche forma di disabilità, e di questi  la metà è portatore di un deficit così grave da perdere l’autosufficienza.L’ictus è più frequente dopo i 55 anni, la sua prevalenza raddoppia successivamente ad ogni decade ; il 75% degli ictus si verifica nelle persone con più di 65 anni. La prevalenza di ictus nelle persone di età 65-84 anni è del 6,5% (negli uomini 7,4%, nelle donne 5,9%).La definizione di ictus comprende:",
  "Fattori di rischio": "Fattori di rischio per ictus ischemico: Fattori di rischio per ictus emorragico",
  "Sintomi": "È fondamentale riconoscere immediatamente i sintomi dell’ictus per poter intervenire quanto prima possibile; questo consente di salvare vite e di limitare la comparsa di disabilità. I sintomi principali, che si manifestano improvvisamente, sono:L’alterazione anche di uno solo dei tre segni è altamente suggestiva per un ictus. È importante annotare l’orario della comparsa dei primi sintomi perché presso ospedali specializzati, dotati di “stroke unit” è possibile sottoporre il paziente colpito da ictus ischemico ad una terapia trombolitica (cioè che scioglie l’eventuale trombo) entro 3 ore dall’esordio dei sintomi.Altri segni che possono aiutare nella identificazione dell’ictus sono: L’acronimo FAST, usato dagli americani, consente di ricordare facilmente alcuni test da fare nel sospetto che una persona sia stata colpita da un ictus(Cincinnati Prehospital Stroke Scale).:",
  "Diagnosi": "La diagnosi di ictus viene fatta in ospedale mediante l’ausilio di: ",
  "Terapia": "Trattamento dell’ictus ischemico in fase acutaTrattamento dell’ictus emorragicoFase post ricovero\nLa fase che segue il ricovero è la più delicata perché vanno affrontati i problemi riguardanti il paziente, la famiglia, l'organizzazione degli interventi a livello territoriale; vanno programmati interventi riabilitativi (fisioterapia, logopedia e terapia occupazionale), interventi clinici (terapia antipertensiva, ipolipemizzante, antiaggregante, anticoagulante e il trattamento delle comorbidità, come il diabete, la bronchite cronica, la malattia renale cronica ecc.).\nFondamentale è l'attenzione verso lo stile di vita sano (alimentazione sana e abolizione del fumo), già descritto nella sezione prevenzione; una attenzione particolare va rivolta verso l'attività fisica; infatti è dimostrato che una grave menomazione funzionale causa sedentarietà, che, a sua volta, causa nuove menomazioni, nuove limitazioni funzionali, nuova disabilità con riduzione ulteriore dell'attività motoria e della partecipazione sociale.\nEsistono programmi specifici di attività fisica adattata per pazienti con esiti cronici di ictus cerebrale.\nInoltre non va dimenticato il sostegno psicologico al paziente, con la prevenzione alla depressione e il sostegno alla famiglia.",
  "Prevenzione": "Il 50% degli ictus ischemici potrebbe essere prevenuto modificando lo stile di vita; infatti esso è attribuibile ad una mancata adesione ad uno stile di vita salutare (astensione dal fumo, regolare attività fisica e alimentazione corretta)Come si può prevenire l’ictus:"
}
```

## Next steps

- I'd like to add a synonym search to get terms even if the patient uses a different name.
