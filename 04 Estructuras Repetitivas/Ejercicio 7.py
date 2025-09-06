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