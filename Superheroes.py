Spider_Man = 0
Iron_Man = 0
Wonder_Woman = 0
Batman = 0

print("Pregunta 1: ¿Cuál es tu habilidad favorita: ")
print("1) Agilidad")
print("2) Inteligencia")
print("3) Fuerza")
print("4) Misterio")

Q1 = int(input("Escribe tu respuesta: "))

if Q1 == 1:
    Spider_Man += 1
elif Q1 == 2:
    Iron_Man += 1
elif Q1 == 3:
    Wonder_Woman += 1
elif Q1 == 4:
    Batman += 1
else:
    print("Intentalo de nuevo")

print("Pregunta 2: Qué te motiva a luchar?: ")
print("1) La Justicia")
print("2) La Ciencia")
print("3) La Verdad")
print("4) La Oscuridad Interior")

Q2 = int(input("Elige la opción que desees: "))

if Q2 == 1:
    Spider_Man += 1
elif Q2 == 2:
    Iron_Man += 1
elif Q2 == 3:
    Wonder_Woman += 1
elif Q2 == 4:
    Batman += 1
else:
    print("Intentalo de nuevo")

print("Pregunta 3: Cuál es tu ciudad ideal?: ")
print("1) Nueva York")
print("2) Los Angeles")
print("3) Temiscira")
print("4) Gotham")

Q3 = int(input("Elige la opción que te identifique: "))

if Q3 == 1:
    Spider_Man += 1
elif Q3 == 2:
    Iron_Man += 1
elif Q3 == 3:
    Wonder_Woman += 1
elif Q3 == 4:
    Batman += 1
else:
    print("Intentalo de nuevo")

print("Spider Man: ", Spider_Man)
print("Iron Man: ", Iron_Man)
print("Wonder Woman: ", Wonder_Woman)
print("Batman: ", Batman)