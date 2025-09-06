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