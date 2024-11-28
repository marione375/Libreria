import datetime
ora = datetime.datetime.now()
def Aggiunta(ListaLibri):
    print("Ha selezionato aggiunta libro.\n")
    risposta = 0
    while risposta == 0 or risposta =="no":
        Titolo = input("Inserisca il titolo del libro\n")
        Autore = input("Chi è l'autore del libro?\n")
        risposta = input (f"{Titolo} di {Autore}, è corretto?\n [si o no]\n")
        if risposta == "si":
            print(f"la ringrazio per la sua aggiunta ({ora})")
            ListaLibri.append(f"{Titolo} di {Autore}")
        elif risposta != "si" or risposta != "no":
            print("la prego di selezionare o si o no")
def Prestito(ListaLibri,ListaLibriPrestati):
    print("Ha selezionato il prestito del libro")
    quantitàprestito = int(input("Quanti libri desidera prendere in prestito?\n"))
    while quantitàprestito > 0:
        quantitàprestito = quantitàprestito - 1
        while risposta == 0 or risposta =="no":
            Titolo = input("Inserisca il titolo del libro\n")
            Autore = input("Chi è l'autore del libro?\n")
            risposta = input (f"{Titolo} di {Autore}, è corretto?\n [si o no]\n")
            if risposta == "si":
                controllo = ListaLibri.count(f"{Titolo} di {Autore}")
                if controllo > 0:
                    print("il libro o i libri sono disponibili, desidera prelevarli")
                    ListaLibri.remove(f"{Titolo} di {Autore}")
                    ListaLibriPrestati.append(f"{Titolo} di {Autore}")
                else :
                    print("il libro non è disponibile")
                if quantitàprestito < 0:
                    print("perfavore digiti un numero positivo")
                else:
                    print("Servizio effettuato")
            elif risposta != "si" or risposta != "no":
                print("la prego di selezionare o si o no")
def Restituzione(ListaLibri,NomeInput,CognomeInput,ListaLibriPrestati):
    print("Ha selezionato la restituzione del libro")
    Titolo = input("Inserisca il titolo del libro\n")
    Autore = input("Chi è l'autore del libro?\n")
    Codicelibro = input("Inserisca il codice libro\n")
    risposta = input (f"{Titolo} di {Autore}, codice {Codicelibro}\n è corretto?\n [si o no]\n")
    if risposta == "si":
        if Codicelibro >= 6969696:
            print("Codice incorretto")
        else:
            print(f"la ringrazio per la restituzione {CognomeInput} {NomeInput}({ora})")
            ListaLibri.append(f"{Titolo} di {Autore}")
            ListaLibriPrestati.remove(f"{Titolo} di {Autore}")
    elif risposta != "si" or risposta != "no":
        print("la prego di selezionare o si o no")
def Catalogo(ListaLibri):
    for Lista in ListaLibri:
        print(Lista)
def CatalogoPrestiti(ListaLibriPrestati):
    for Lista1 in ListaLibriPrestati:
        print(Lista1)
