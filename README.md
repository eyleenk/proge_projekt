Probleemi kirjeldus - Sudoku generaator. Programmeerimiskeel: Python. Genereerib 9x9 ruudust koosneva interaktiivse mängulaua. Kasutamiseks vajalikud moodulid/paketid: numpy, pygame ja random.


Eesmärgid ja lahenduse ülevaade - Eesmärgiks luua isiklik Sudokut genereeriv programm, mis piisavalt kerge ka vanemate riistvarade jaoks ning töötaks ilma internetita.

Tööjaotus rühma liikmete vahel - Idee Rene Vainula. Vigade parandus/täiendused Eyleen Krikk. Ühiselt lahenduste leidmine ja tööjaotus vastavalt vajadusele.

Ajakava ja vahe-eesmärgid/teostatud tööde kirjeldus: Vahe-eesmärkide paremaks ülevaateks loodud issue süsteemi tasklist, mida saab vastavalt arengule teostatuks märkida.  
*Algne kood valmis märtsi lõpus. *Täiendused/parandused/projekti kirjeldus aprilli algus/keskpaik.  
*Aprilli algul lisatud algne versioon töötavast koodist, kus imporditud mänguks vajalikud liidesed, loodud funktsioon main, määratud mängulaua suurus ja disain ning algväärtustatud laud, mis esialgselt numbritega täidetud. Joonistatud esialgne mängulaud.  
*Aprilli keskpaigas lisatud esimene täiendus, kus olevad muudatused kasutajaliideses: Lisatud board muutuja algväärtustamine, lisatud sisestamise funktsioon insert, mis lubab kasutajal lauale väärtusi sisestada. Numbrilaud uueneb automaatselt. Ruudustik tehtud kompaktsemaks/font muudetud. Merge'tud - toimib.  
*Kolmandas versioonis, mis lisatud mai alguses olevad uuendused: - lisatud suvalise laua genereerimine (tehtud kindlaks, et ta on loogiliselt lahendatav ja aktsepteeritud sudoku reeglite järgi) ning lisaks võimalus lahendada keskmise raskusasmega sudokut.  
*Neljas versioon valmis mai keskpaigaks: lisatud sai võidusõnum ja lahenduse kontroll võrreldes algsudokuga. Kontrollitud kogu programmi töötamist ja lahendamist. Toimib  

Projekti kokkuvõte: loodud Sudoku mäng, mis kasutab pygame'i graafilise kasutajaliidese loomiseks.
Kood sisaldab järgmisi olulisi funktsioone: 
*board, current ja answer on 9x9 massiivid, mis esindavad Sudoku lauda.  
*Board on mängija nähtav laud, current hoiab jooksvat mänguseisu ja answer sisaldab õiget lahendust.  
*PossibleValueAtPosition on funktsioon, mis tagastab kõik võimalikud väärtused antud positsioonil.  
*Solution_Count on funktsioon, mis loendab lahenduste arvu antud laual.  
*SudokuSolver on funktsioon, mis lahendab Sudoku mõistatuse.  
*DigHoles on funktsioon, mis kaevab auke täielikult lahendatud lauale, et luua mõistatus.  
*generate_board on funktsioon, mis genereerib uue laua.  
*insert on funktsioon, mis lisab kasutaja sisestatud väärtuse lauale.  
*main on peamine funktsioon, mis käivitab mängu.  
*isWin on funktsioon, mis kontrollib, kas kasutaja on võitnud.  
Lõpuks genereeritakse laud, kopeeritakse see current'isse ja käivitatakse mäng.  

Projekti tugevused ja nõrkused, võimalused arendamiseks:  
*Kindlasti saaks koodi optimeerida, teha kiiremaks, lühemaks.  
*Saaks täiustada algoritme ja kasutajakogemust oleks võimalik parandada.  
*Tasakaal koodi lihtsuse ja jõudluse optimeerimise vahel.  
