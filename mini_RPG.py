
import random

jugador_1 = 100
enemigo = 100

print ("Jugador 1 = 100 |  Enemigo = 100\n")

while jugador_1 > 0 and enemigo > 0:
    
    accion = int(input("Jugador 1, ¿Qué deseas hacer?\n1. Atacar\n2. Curar\nElige: "))
    print("\n" + "-"*40 + "\n")

    if accion == 1:
        atacar = random.randint(1, 10)
        enemigo -= atacar
        print("Has atacado al enemigo por", atacar, "puntos")
        print("La vida del enemigo es:", enemigo)
        print("\n" + "-"*40 + "\n")
     
    elif accion == 2:
        curar = random.randint(1, 10)   
        jugador_1 += curar
        print("Te has curado", curar, "puntos")
        print("Tu vida actual es:", jugador_1)
        print("\n" + "-"*40 + "\n")
     
    if enemigo > 0:
        dano_enemigo = random.randint(1, 10)
        jugador_1 -= dano_enemigo
        print("El enemigo te ha atacado por", dano_enemigo, "puntos")
        print("tu vida actual es:", jugador_1)
        print("\n" + "-"*40 + "\n")
     
        print("Tu vida =", max(0,jugador_1), "| Enemigo =", max(0, enemigo))
        print("\n" + "-"*40 + "\n")
    
    if jugador_1 <= 0:
        print("El juego ha terminado, fuiste derrotado 😔")
        break
    
    if enemigo <= 0:
        print("Has vencido al enemigo!! 🤖")
        break
    
print("Espero que te hayas divetido")