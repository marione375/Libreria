import random
import datetime
from libro import Aggiunta
from libro import Prestito
from libro import Restituzione
from libro import Catalogo
ora = datetime.datetime.now()
ListaLibri = ["Harry Potter e la pietra filosofale di JK Rowling", "Harry Potter e la camera dei segreti di JK Rowling","Harry Potter e il prigioniero di azkaban","Harry Potter e il calice di fuoco di JK Rowling","HungryGames la ragazza con l'uccello di fuoco",]
programma = 1
while programma!= "no":
    NomeInput = input("Inserisca il suo nome\n")
    CognomeInput =input("Inserisca il suo cognome\n")
    selezione = input("salve come posso aiutarla\n 1) aggiunta libro\n 2) prestito libro\n 3) riportato un libro\n 4) ricerca nel catalogo\n")
    if selezione == "1":
        Aggiunta(ListaLibri)
    elif selezione == "2":
        Prestito(ListaLibri)
    elif selezione == "3":
        Restituzione(ListaLibri,NomeInput,CognomeInput)
    elif selezione == "4":
        Catalogo(ListaLibri)
    else:
        programma = input ("Desideri chiudere il programma?\n [si o no]")
else:
    print ("programma spento")
