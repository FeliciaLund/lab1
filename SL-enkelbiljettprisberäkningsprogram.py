#SL-enkelbiljettprisberäkningsprogram med GUI

from tkinter import *

def beräknaPris(antal): 
    return 26*antal

def konvertera(indata):
    utmatning["text"] = str(beräknaPris(indata))

# Sätter konstanter för textstorlek och fonter
STORLEK = 20
TIMES = ("Times", STORLEK)
COURIER = ("Courier", STORLEK)

# Skapar rotfönstret
rot = Tk()
rot.title("SL-enkelbiljettprisberäkningsprogram")
huvudRam = Frame(rot)
huvudRam.grid()

# Sätter informationstexten överst
info = Label(text = "Hej och välkommen till Alvin och Felicias SL-enkelbiljettprisberäkningsprogram! Hurra! :D", font = TIMES)
info.grid(row = 0, column = 0, padx = 5, pady = 5)

# Skapar den vita inmatningsrutan
inmatning = Entry(font=COURIER, width = 15)
inmatning.grid(row=1, column = 0, padx = 5, pady = 5, sticky = E)
ledtext = Label(text = "antal enkelbiljetter", font=TIMES)
ledtext.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)

# Skapar utmatningsfältet
utmatning = Label(font=COURIER, width = 15)
utmatning.grid(row=2, column = 0, padx = 5, pady = 5, sticky = E)
svarstext = Label(text = "kr", font=TIMES)
svarstext.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = W)

# Skapar Konvertera-knappen
knapp = Button(text = "Beräkna", font = TIMES, command = lambda: konvertera(float(inmatning.get())))
knapp.grid(row = 3, column = 1, padx = 5, pady = 5)

# Startar slingan som väntar på inmatning...
rot.mainloop()


