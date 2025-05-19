# **Praktiline Osa: Projekti Idee: Hierarhiline Ressursihaldusmäng

![image](https://github.com/user-attachments/assets/db2c5306-277b-4732-bd33-1be6b2637019)


## Sprint 1 
käigus keskenduti põhistruktuuri loomisele ja mängu põhiandmete initsialiseerimisele. See hõlmas põhiklasside kirjutamist, mis haldavad mängu ressursse ja platvorme:

- Platvormi klass: Lõin Platform-klassi, mis esindab iga tasandit mängus. See sisaldab meetodeid ressursside jaotamiseks igale platvormile, tagades, et platvormi ressursside arv ei ületaks selle olemasolevat hulka.

- Ressursiklass: Resource-klass rakendati mängule kättesaadavate ressursside haldamiseks. Ressursside hulka saab mängu edenedes vähendada, tagades, et ressursse kasutatakse strateegiliselt.

- Mänguklass: Mänguklass loodi mängu seisundi initsialiseerimiseks, koos tasemete arvu ja esialgse ressursside arvuga. See haldab platvormide loomist ja ressursside jaotamist tasemete vahel.

## Sprint 2

- Juhuslik ressursside jaotamine: Funktsiooni random.randint() kasutati selleks, et simuleerida ettearvamatuid ressursikoguseid, mis jaotatakse igal platvormil. See toob kaasa varieeruvuse ja võimaliku riski, kuna mängijad ei saa olla kindlad, kui palju nad saavad igalt platvormilt võtta.

- Ressursside ammendumise käsitlemine: Platvormide ja ressursside klassid kohandati nii, et nad suudaksid käsitleda juhtumeid, kus taotletud ressursid ületavad olemasolevaid ressursse, mis kujutab endast stsenaariumi, kus ressursid võivad otsa saada - see on tõenäoliselt risk, mida mängijad peavad juhtima.

## Sprint 3
raames keskenduti ellujäämismängu täiustamisele ja mängija valikute parandamisele. See sprint hõlmas tõenäoliselt ressursside haldamise süsteemi täiustamist ja mängumehaanika laiendamist:

- Mängusilmuse täiustused: Välja töötati meetod run(), et simuleerida tegelikku mängimist. See kordab läbi kõik platvormid, kasutades juhusliku numbrigeneraatori, et otsustada, kui palju ressursse saab võtta. See lisab mängule sügavust, kuna mängija peab haldama ressursse mitmel tasandil.

- Mänguvoo täiustamine: Täiustasin ressursside jälgimise viisi kogu mängu jooksul. Pärast iga platvormi ressursside jaotamist uuendatakse järelejäänud ressursse ja tulemus trükitakse mängijale nähtavale. See tagab, et mängija saab jälgida oma edusamme ja kohandada oma strateegiat vastavalt.
