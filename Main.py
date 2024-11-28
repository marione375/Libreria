from libro import Aggiunta,Prestito,Restituzione,Catalogo,CatalogoPrestiti
ListaLibri = ["Harry Potter e la pietra filosofale di JK Rowling", "Harry Potter e la camera dei segreti di JK Rowling","Harry Potter e il prigioniero di azkaban","Harry Potter e il calice di fuoco di JK Rowling","HungryGames la ragazza con l'uccello di fuoco",]
ListaLibriPrestati = ["Harry Potter e l'ordine della fenice di JK Rowling","Harry Potter ed il principe mezzosangue di JK Rowling","Harry Potter ed i doni della morte di JK Rowling","Harry Potter e la maledizione dell'erede di JK Rowling"]
programma = 1
NomeInput = input("Inserisca il suo nome\n")
CognomeInput =input("Inserisca il suo cognome\n")
while programma != "si":
    selezione = input("salve come posso aiutarla\n 1) aggiunta libro\n 2) prestito libro\n 3) restituzione di un libro\n 4) ricerca nel catalogo\n 5) lista libri prestati\n")
    if selezione == "1":
        Aggiunta(ListaLibri)
    elif selezione == "2":
        Prestito(ListaLibri,ListaLibriPrestati)
    elif selezione == "3":
        Restituzione(ListaLibri,NomeInput,CognomeInput,ListaLibriPrestati)
    elif selezione == "4":
        Catalogo(ListaLibri)
    elif selezione == "5":
        CatalogoPrestiti(ListaLibriPrestati)
    else:
        programma = input ("Desideri chiudere il programma?\n [si o no]\n")
else:
    print ("programma spento")
