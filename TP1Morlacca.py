# Ejercicio 1
print("Hola Mundo!")

# Ejercicio 2
nombre = input("Introduce tu nombre: ")
print(f"Hola {nombre}!")

# Ejercicio 3
nombreCompleto = input("Ingrese su nombre completo: ")
edad = input("Ingrese su edad: ")
pais = input("Ingrese su país: ")
print(f"Soy {nombreCompleto}, tengo {edad} años y vivo en {pais}.")

# Ejercicio 4
import math
radio = float(input("Ingrese el radio del círculo: "))
print(f"El área es: {math.pi * radio ** 2} y el perimetro es : {2 * math.pi * radio}")

# Ejercicio 5
segundos = int(input("Ingrese el número de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos, equivalen a {horas} horas.")

# Ejercicio 6
numero = int(input("Ingrese un número: "))
for i in range(1, 10):
    print(f"{numero} x {i} = {numero * i}")

# Ejercicio 7
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
print(f"Mostrando cuentas para {num1} y {num2}")
print(f"La suma es: {num1 + num2}")
print(f"La resta es: {num1 - num2}")
print(f"La multiplicación es: {num1 * num2}")
print(f"La división es: {num1 / num2}")

# Ejercicio 8
altura = float(input("Ingrese su altura en metros: "))
peso = float(input("Ingrese su peso en kilogramos: "))
imc = peso / (altura ** 2)
print(f"Su IMC es: {imc}")

# Ejercicio 9
temperatura = float(input("Ingrese la temperatura en grados Celsius: "))
temperatura_fahrenheit = (temperatura * 9/5) + 32
print(f"La temperatura en grados Fahrenheit es: {temperatura_fahrenheit}")

# Ejercicio 10
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))
prom = (num1 + num2 + num3) / 3
print(f"El promedio de los números es: {prom}")