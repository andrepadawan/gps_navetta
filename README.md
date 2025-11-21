Come <b>tanti</b> altri progetti questo codice è nato per far fronte a un problema. Chiunque abbia mai usato dei 
mezzi pubblici si è trovato a dire: ma quando passa la navetta?

Questo progetto nasce dall'esigenza di offrire un servizio gratuito di trasporto di persone, senza finalità commerciali,
negli ambiti di fiere e manifestazioni artistiche con mezzi privati, al più 8 posti senza conducente.

Questa app è scritta in python e gira su Raspberry Pi, si interfaccia con l'autista con una pagina html locale con Flask.
L'autista inizierà il suo viaggio dopo aver premuto il tasto "naviga" sull'interfaccia, che dà il via alla trasmissione 
delle coordinate gps del veicolo a un database su Firebase.
Da lì, la pagina web lato client è in grado di mostrare la posizione della navetta su una mappa (ottenuta con Leafleet) per dare 
una sicurezza relativa all'esistenza della navetta (in primis) e sui tempi stimati di arrivo di quest'ultima.
