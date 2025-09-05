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