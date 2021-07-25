# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#                                                                   CALCULATRICR (GRAPHIQUE)
# \\\\\\\\\\\\\\\\\\\

# --------------
# IMMPORTATION :
# --------------
from tkinter import *  # Tkinter


# ---------
# CLASSE :
# ---------
class Calculator():
    def __init__(self):  # Construction
        self.phase1 = 0  # Premier nombre
        self.phase2 = 0  # Deuxième nombre
        self.final = 0  # Valeur finale
        self.entry = StringVar()  # Capte les valeurs écrit
        self.text = ""  # Nombre écrir par l'utilisateur
        self.signe = ""  # Type d'opération
        self.entry.set("operation")

    def init(self):  # Initialisation
        self.phase1 = 0  # Premier nombre
        self.phase2 = 0  # Deuxième nombre
        self.final = 0  # Valeur finale
        self.text = ""  # Nombre écrir par l'utilisateur
        self.signe = ""  # Type d'opération

    def afficher_Nb(self):  # Afficher les nombre sur écran
        self.entry.set(self.text)

    def operation(self):  # Vérification du type d'opération
        try:
            if "+" in self.text:
                self.Plus()
            elif "-" in self.text:
                self.Sous()
            elif "/" in self.text:
                self.Div()
            elif "X" in self.text:
                self.Mult()
        except:
            self.entry.set("ERROR")
            self.init()

    def Plus(self):  # Addition
        nb = self.text.split("+")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 + self.phase2


        dec = str(self.final).split(".")[1]
        if(dec == "0"):
            self.final = str(self.final).split(".")[0]


        self.entry.set(str(self.final))
        self.init()

    def Sous(self):  # Soustraction
        nb = self.text.split("-")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 - self.phase2

        dec = str(self.final).split(".")[1]
        if (dec == "0"):
            self.final = str(self.final).split(".")[0]

        self.entry.set(str(self.final))
        self.init()

    def Div(self):  # Division
        nb = self.text.split("/")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 / self.phase2

        dec = str(self.final).split(".")[1]
        if (dec == "0"):
            self.final = str(self.final).split(".")[0]

        self.entry.set(str(self.final))
        self.init()

    def Mult(self):  # Multiplication
        nb = self.text.split("X")
        self.phase1 = float(nb[0])
        self.phase2 = float(nb[1])
        self.final = self.phase1 * self.phase2

        dec = str(self.final).split(".")[1]
        if (dec == "0"):
            self.final = str(self.final).split(".")[0]

        self.entry.set(str(self.final))
        self.init()


# ------------
# FONCTIONS :
# ------------
def Button1():  # Actionnerle bouton 1
    calculatrice.text += "1"
    calculatrice.entry.set(calculatrice.text)


def Button2():  # Actionnerle bouton 2
    calculatrice.text += "2"
    calculatrice.entry.set(calculatrice.text)


def Button3():  # Actionnerle bouton 3
    calculatrice.text += "3"
    calculatrice.entry.set(calculatrice.text)


def Button4():  # Actionnerle bouton 4
    calculatrice.text += "4"
    calculatrice.entry.set(calculatrice.text)


def Button5():  # Actionnerle bouton 5
    calculatrice.text += "5"
    calculatrice.entry.set(calculatrice.text)


def Button6():  # Actionnerle bouton 6
    calculatrice.text += "6"
    calculatrice.entry.set(calculatrice.text)


def Button7():  # Actionnerle bouton 7
    calculatrice.text += "7"
    calculatrice.entry.set(calculatrice.text)


def Button8():  # Actionnerle bouton 8
    calculatrice.text += "8"
    calculatrice.entry.set(calculatrice.text)


def Button9():  # Actionnerle bouton 9
    calculatrice.text += "9"
    calculatrice.entry.set(calculatrice.text)


def Button0():  # Actionnerle bouton 0
    calculatrice.text += "0"
    calculatrice.entry.set(calculatrice.text)


def ButtonF():  # Actionnerle bouton F
    calculatrice.text += "."
    calculatrice.entry.set(calculatrice.text)


def ButtonP():  # Actionnerle bouton P
    calculatrice.text += "+"
    calculatrice.entry.set(calculatrice.text)


def ButtonS():  # Actionnerle bouton S
    calculatrice.text += "-"
    calculatrice.entry.set(calculatrice.text)


def ButtonD():  # Actionnerle bouton D
    calculatrice.text += "/"
    calculatrice.entry.set(calculatrice.text)


def ButtonM():  # Actionnerle bouton M
    calculatrice.text += "X"
    calculatrice.entry.set(calculatrice.text)


def ButtonE():  # Actionnerle bouton E
    calculatrice.operation()


def ButtonC():  # Actionnerle bouton c
    calculatrice.entry.set("")
    calculatrice.init()


# ----------
# FENETRE :
# ----------
fen = Tk()  # Création de a fenêtre 1e
fen.geometry("250x270")  # Définition de la fenêtre
fen.title("Calculatrice by franck ")  # Titre de la calculatrice
fen.resizable(1, 1)
fen["bg"] = "red"  # Couleur de la fenêtre
fen["relief"] = "raised"  # Profondeur de la fenêtre
# ------------
# PROGRAMME :
# ------------
# Création instance
calculatrice = Calculator()


Grid.rowconfigure(fen,0,weight=1)
Grid.rowconfigure(fen,1,weight=1)
Grid.rowconfigure(fen,2,weight=1)
Grid.rowconfigure(fen,3,weight=1)
Grid.rowconfigure(fen,4,weight=1)
Grid.columnconfigure(fen,0,weight=1)
Grid.columnconfigure(fen,1,weight=1)
Grid.columnconfigure(fen,2,weight=1)
Grid.columnconfigure(fen,3,weight=1, minsize=60)


# ATTRIBUTS DE LA FENETRE
#########################
# // Ecran calculatrice //
ECRAN = Entry(fen, width=30,font="4", textvariable=calculatrice.entry, bg="black", fg="white", relief=SUNKEN, bd=6, state=DISABLED).grid(row=0, column=0, columnspan=3, sticky="nsew")

# // Bouttons //
B1 = Button(fen, text="1", font="4", command=Button1, bg="white", fg="black").grid(row=1, column=0, sticky="nsew")  # Boutton 1
B2 = Button(fen, text="2", font="4", command=Button2, bg="white", fg="black").grid(row=1, column=1, sticky="nsew")  # Boutton 2
B3 = Button(fen, text="3", font="4", command=Button3, bg="white", fg="black").grid(row=1, column=2, sticky="nsew")  # Boutton 3
B4 = Button(fen, text="4", font="4", command=Button4, bg="white", fg="black").grid(row=2, column=0, sticky="nsew")  # Boutton 4
B5 = Button(fen, text="5", font="4", command=Button5, bg="white", fg="black").grid(row=2, column=1, sticky="nsew")  # Boutton 5
B6 = Button(fen, text="6", font="4", command=Button6, bg="white", fg="black").grid(row=2, column=2, sticky="nsew") # Boutton 6
B7 = Button(fen, text="7", font="4", command=Button7, bg="white", fg="black").grid(row=3, column=0, sticky="nsew")  # Boutton 7
B8 = Button(fen, text="8", font="4", command=Button8, bg="white", fg="black").grid(row=3, column=1, sticky="nsew")  # Boutton 8
B9 = Button(fen, text="9", font="4", command=Button9, bg="white", fg="black").grid(row=3, column=2, sticky="nsew")  # Boutton 9
BC = Button(fen, text="C", font="4", command=ButtonC, bg="white", fg="black", relief=RIDGE).grid(row=4, column=0, sticky="nsew")  # Boutton C (Clear)
B0 = Button(fen, text="0", font="4", command=Button0, bg="white", fg="black").grid(row=4, column=1, sticky="nsew")  # Boutton 0
BF = Button(fen, text=".", font="4", command=ButtonF, bg="white", fg="black").grid(row=4, column=2, sticky="nsew")  # Boutton = (égale)

BP = Button(fen, text="+", font="4", command=ButtonP, bg="Grey", fg="black", relief=RIDGE).grid(row=1, column=3, sticky="nsew")  # Boutton + (addition)
BS = Button(fen, text="-", font="4", command=ButtonS, bg="Grey", fg="black", relief=RIDGE).grid(row=2, column=3, sticky="nsew")  # Boutton - (soustacrtion)
BD = Button(fen, text="/", font="4", command=ButtonD, bg="Grey", fg="black", relief=RIDGE).grid(row=3, column=3, sticky="nsew")  # Boutton / (division)
BM = Button(fen, text="X", font="4", command=ButtonM, bg="Grey", fg="black", relief=RIDGE).grid(row=4, column=3, sticky="nsew")  # Boutton X (multiplication)
BE = Button(fen, text="=", font="4", command=ButtonE, bg="blue", fg="white", relief=RIDGE).grid(row=0, column=3, sticky="nsew")  # Button = (égale)

fen.mainloop()