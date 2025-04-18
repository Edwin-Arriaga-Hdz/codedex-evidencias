
tries = 0
guess = 0

while guess != 10 and tries != 3:
    tries += 1
    guess = int(input("Intenta Adivinar el número:  ")) 
    if tries == 1 and guess != 10:
        print("!Vamos puedes lograrlo¡")
    elif tries == 2 and guess != 10:
        print("Intentalo de nuevo, no te rindas")
    elif tries == 3 and guess != 10:
        print("Lo siento, se han terminado las oportunidades")
    else:
        print("Lo has logrado")

