
import random

player1 = 100
mutant_bug = 100
interstellar_maggot = 200
galactic_crab = 300

print("\nWelcome interstellar traveler, in this journey forward unknown places, you will have to face and battle against terrible creatures.")
print("-"*131)

name = str(input("What's your name brave cosmonaut: "))
print("-"*45)

print(f"Are you ready for it, let's start {name}?")
print("-"*40)

print("\nThese are the planets that you'll have to pass trough:\n\n1)🌌 Sameria \n2)🪐 Galactim \n3)🌠 Ensiarus\n ")
print("-"*159)

print(f"You're in Sameria, a planet 2 light years far from the earth, everthing looked quiet, when suddenly a mutant bug appeared, now it's time to fight {name}, get ready")
print("-"*159)

print(f"\n{name} = 100 hp     |     Mutant Bug = 100 hp\n")
print("-"*45)

while player1 > 0 and mutant_bug > 0:
        
        action = int(input("¿What do you want to do?\n1) Attack\n2) Cure\n> "))
        print("-"*42)

        if action == 1:
            attack = random.randint(5, 10)
            mutant_bug -= attack
            print("You hit the Mutant Bug for", attack, "points")
            print("Mutant Bug =", mutant_bug, "hp")
            print("-"*42)
        
        if action == 2:
            cure = random.randint(1, 10)
            player1 += cure
            print("You've cured for", cure, "hp")
            print(f"{name} =", player1, "hp" )
            print("-"*28)

        if mutant_bug > 0:
            bug_attack = random.randint(1, 10)
            player1 -= bug_attack
            print("You've been attacked for", bug_attack, "points")
            print("You have", player1, "hp")
            print("-"*43)
            print("You have", max(0,player1), "hp" " | Mutant Bug", max(0, mutant_bug), "hp")
            print("-"*43)

        if player1 <= 0:
            print("\nYou have been defeated by Mutant Bug")
            print("Good luck for the next time\n")
            break

        if mutant_bug <= 0 and player1 > 0:
            print("You've won, now it's time to go to other planet")
            print("-"*40)
            print("\nGalactim is an isolated land, you've realized that there are many holes around you")
            print("Look out!!!, omg!!, it's the terrible Interstellar Maggot")
            print("\nIt's time to fight against the Interstellar Maggot\n")
            print("-"*50)
            print(f"{name} = {player1}        |      Interstellar Maggot = 200") 
            print("-"*50 + "\n")
            
            while player1 > 0 and interstellar_maggot > 0:
        
                action2 = int(input(f"¿What do you want to do?:\n1) Attack\n2) Cure\n> "))
                print("-"*40)
    
                if action2 == 1:
                    attack2 = random.randint(10,20)
                    interstellar_maggot -= attack2
                    print("You hit the Interstellar Maggot for", attack2, "points")
                    print("Interstellar Maggot", interstellar_maggot, "points")
                    print("-"*40)
    
                elif action2 == 2:
                    cure2 = random.randint(10,15)
                    player1 += cure2
                    print("You've cured for", cure2, "points")
                    print(f"{name} =", player1, "hp" )
                    print("-"*40)
    
                if interstellar_maggot > 0:
                    maggot_attack = random.randint(1, 15)
                    player1 -= maggot_attack
                    print("You've been attacked for", maggot_attack, "points")
                    print("You have", player1, "hp")
                    print("-"*40)
        
                    print("You have", max(0,player1), "hp" " | Interstellar Maggot", max(0, interstellar_maggot), "hp")
                    print("-"*43)

    
                if player1 <= 0:
                    print("\nYou have been defeated by the Interstellar Maggot")
                    print("You almost got it\n")
                    break
        
                if interstellar_maggot <= 0 and player1 > 0:
                    print("\nWell done!!, you just defeated the Interstellar Maggot, are you ready for the next and final boss? 😈\n")
                    print("-"*60)
                    print("\nNow it's time to fight against the Galactic Crab\n")
                    print("-"*40)
                    print(f"{name} = {player1}        |      Galactic Crab = 300") 
                    print("-"*40)

                    while player1 > 0 and galactic_crab > 0:
        
                        action3 = int(input(f"¿What do you want to do?:\n1) Attack\n2) Cure\n> "))
                        print("-"*40)
    
                        if action3 == 1:
                            attack3 = random.randint(10,20)
                            galactic_crab -= attack3
                            print("You hit the Galactic Crab for", attack3, "points")
                            print("Galactic Crab", galactic_crab, "points")
                            print("-"*40)
    
                        elif action3 == 2:
                            cure3 = random.randint(10,15)
                            player1 += cure3
                            print("You've cured for", cure3, "points")
                            print(f"{name} =", player1, "hp" )
                            print("-"*40)
    
                        if galactic_crab > 0:
                            crab_attack = random.randint(1, 15)
                            player1 -= crab_attack
                            print("You've been attacked for", crab_attack, "points")
                            print("You have", player1, "hp")
                            print("-"*40)
        
                            print("You have", max(0,player1), "hp" " | Galactic Crab", max(0, galactic_crab), "hp")
                            print("-"*43)

    
                        if player1 <= 0:
                            print("\nYou have been defeated by the Galactic Crab")
                            print("You were so too close")
                            break
        
                        if galactic_crab <= 0:
                            print("Well done!!, you have domain the space, you are the strongest cosmonaut in the universe 🤖\n")
                            break