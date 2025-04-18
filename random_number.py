
import random

numero = random.randint(1, 10)

guess = 0
tries = 0

while numero != guess and tries != 3:
    guess = int(input("Adivina el número del 1 al 10: "))
    tries += 1
    if guess == numero:
        print("Felicidades lo has logrado!!")
    elif tries == 1:
        print("Una oportunidad más")    
    elif tries == 2:
        print("Vuelve a intentarlo")
    elif guess != numero:
        print(f"El numero era {numero}")    
