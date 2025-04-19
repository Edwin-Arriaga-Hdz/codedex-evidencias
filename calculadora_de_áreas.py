
Triangulo = 0
Rectangulo = 0
Cuadrado = 0
Circulo = 0 

lado = ""
base = ""
altura = ""
radio = ""
area = ""

print(f"Bievenido a la calculadora de áreas\n")
print("1) Triángulo")
print("2) Rectangulo")
print("3) Cuadrado")
print("4) Círculo")
print("5) Salir\n")

figura = int(input("Escoge la figura que quieras calcular: "))

while figura in range (1, 6):
    if figura == 1:
     base = float(input("Ingresa el valor de la base: " ))
     altura = float(input("Ingresa el valor de la altura: "))
     area = base*altura/2
     print("El área del triángulo es:", area)
    elif figura == 2:
     base = float(input("Ingresa el valor de la base: " ))
     altura = float(input("Ingresa el valor de la altura: "))
     area = base*altura
     print("el área del rectangulo es: ", area)
    elif figura == 3:
     lado = float(input("Ingresa el valor del lado: " ))
     area = lado ** 2
     print("El área del cuadrado es:", area)
    elif figura == 4:
     radio = float(input("Ingresa el valor del radio: " ))
     area = radio*3.1416**2
     print("El área del circulo es: ", area)
    else:
     print("Gracias por utilizar esta calculadora de áreas 😁")
     break
 
    figura = int(input("\n¿Quieres calcular otra figura? Elige una opción:\n1) Triángulo\n2) Rectángulo\n3) Cuadrado\n4) Círculo\n5) Salir\n\nTu elección: "))