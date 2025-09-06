"""
    1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
    (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
"""

for i in range(101):
    print(i)

"""
    2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
    dígitos que contiene.
"""

numero = input("Ingrese un numero entero")
print(f"El numero tiene {len(numero)} digitos")

"""
    3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
    dados por el usuario, excluyendo esos dos valores.
"""

num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
suma = 0

for i in range(num1 + 1, num2):
    suma += i
    
print(f"La suma de los numeros comprendidos entre {num1} y {num2} es {suma}")

"""
    4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
    secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
    un 0.
"""

num = None
suma = 0

while num != 0:
    num = int(input("Ingrese un numero: "))
    suma += num

print(f"La suma de los numeros ingresados es {suma}")

"""
    5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
    programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""

import random

intentos = 0
ingreso = None
numero = random.randint(0, 9)

while ingreso != numero:
    ingreso = int(input("Ingrese un numero del 0 al 9: "))
    intentos += 1

print(f"Acertaste! Era el numero {ingreso}! Eso te llevó {intentos} intentos")

"""
    6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
    entre 0 y 100, en orden decreciente.
"""

for i in range(100, -1, -2):
    print(i)

"""
    7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
    número entero positivo indicado por el usuario.
"""

numero = int(input("Ingrese un numero entero positivo: "))
suma = 0
explicacion = ""

for i in range(numero + 1):
    suma += i
    if i < numero:
        explicacion += f"{i} + "
    else:
        explicacion += f"{i}"
        
print(explicacion)
print(f"La suma de los numeros entre 0 y {numero} es {suma}")

"""
    8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
    programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
    negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
    menor, pero debe estar preparado para procesar 100 números con un solo cambio).
"""

limite = 3 # Cambiar a 100
pares = 0
impares = 0
negativos = 0
positivos = 0


for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"Numeros pares: {pares}")
print(f"Numeros impares: {impares}")
print(f"Numeros positivos: {positivos}")
print(f"Numeros negativos: {negativos}")

"""
    9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
    media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
    poder procesar 100 números cambiando solo un valor).
"""

limite = 3  # cambiar a 100
suma = 0

for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    suma += numero

media = suma / limite
print(f"La media de los {limite} numeros ingresados es: {media}")

"""
    10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
    usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
"""

num = int(input("Ingrese un numero y lo damos vuelta: "))
invertido = 0

while num > 0:
    digito = num % 10 # extrae el ultimo digito
    invertido = invertido * 10 + digito # vamos armando el numero invertido 
    num //= 10 # para saber cuando detener el while

print(f"El numero invertido es: {invertido}")
