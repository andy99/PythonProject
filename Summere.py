# While loop

def summere(tall):
    print(tall,"Tall har verdi")
    while tall < 6:
        tall = tall + tall
        print(tall,"tall har verdi")

Antallinn = input("Tast et tall: " )
tall = int(Antallinn)
summere(tall)
