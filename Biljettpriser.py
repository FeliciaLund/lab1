# Alvin Hallander och Felicia Lund 2024.09.30.

# Tar indata
dagarPerVecka = int(input("Hur många dagar i veckan åker du med kollektivtrafiken? (svara med en siffra) "))
rabatterad = input("Får du köpa rabatterad biljett? ").lower()
if rabatterad == "ja":
    rabatterad = True
elif rabatterad == "nej":
    rabatterad = False
else:
    print("Kör programmet igen och svara ja eller nej!")

# Definierar kostnaden
if rabatterad:
    månadspris = 650
else:
    månadspris = 1020

if rabatterad:
    totaltEnkelpris = 26*2*4*dagarPerVecka # Detta ger 4 veckor (28 dagar), månadskortet gäller i 30 dagar, men vi bedömmer att det är inom felmarginal.
else:
    totaltEnkelpris = 42*2*4*dagarPerVecka

# Jämför priser och ger utdata
if månadspris > totaltEnkelpris:
    print("Du bör köpa enkelbiljetter. Det kommer att kosta", totaltEnkelpris, "kr under en månad. Ett månadskort hade kostat", månadspris, "kr. Det är dyrare!")
else:
    print("Du bör köpa månadskort. Det kommer att kosta", månadspris, "kr. Enkelbiljetter hade totalt kostat", totaltEnkelpris, "kr. Det är dyrare!")

# Exempel med indata 5 och JA
'''
Hur många dagar i veckan åker du med kollektivtrafiken? (svara med en siffra) 5
Får du köpa rabatterad biljett? JA
Du bör köpa månadskort. Det kommer att kosta 650 kr. Enkelbiljetter hade totalt kostat 1040 kr. Det är dyrare!
'''
