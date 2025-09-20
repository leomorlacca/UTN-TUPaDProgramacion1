"""
1) Crear una lista con las notas de 10 estudiantes.
• Mostrar la lista completa.
• Calcular y mostrar el promedio.
• Indicar la nota más alta y la más baja.
"""
notas = [7, 9, 5, 8, 10, 6, 4, 7, 9, 8]
print("Lista de notas:", notas)

total = 0
for nota in notas:
    total += nota
promedio = total / len(notas)
print("Promedio:", promedio)

nota_mas_alta = notas[0]
nota_mas_baja = notas[0]

for nota in notas:
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    if nota < nota_mas_baja:
        nota_mas_baja = nota

print("Nota más alta:", nota_mas_alta)
print("Nota más baja:", nota_mas_baja)


"""
2) Pedir al usuario que cargue 5 productos en una lista.
• Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
• Preguntar al usuario qué producto desea eliminar y actualizar la lista.
"""

productos = []
for i in range(5):
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)

# Mostrar la lista ordenada alfabéticamente
productos_ordenados = sorted(productos)
print("Lista de productos ordenada:", productos_ordenados)

# Preguntar al usuario qué producto desea eliminar
producto_a_eliminar = input("¿Qué producto desea eliminar? ")
productos.remove(producto_a_eliminar)

print("Lista de productos actualizada:", productos)

"""
3) Generar una lista con 15 números enteros al azar entre 1 y 100.
• Crear una lista con los pares y otra con los impares.
• Mostrar cuántos números tiene cada lista
"""

import random
numeros = []
for i in range(15):
    numeros.append(random.randint(1, 100))

print("Lista completa:", numeros)

# Crear listas de pares e impares
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar resultados
print("Números pares:", pares)
print("Números impares:", impares)
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))


"""
4) Dada una lista con valores repetidos: [1, 3, 5, 3, 7, 9, 1, 5, 3]
• Crear una nueva lista sin elementos repetidos.
• Mostrar el resultado.
"""

valores_repetidos = [1, 3, 5, 3, 7, 9, 1, 5, 3]
valores_unicos = []

for valor in valores_repetidos:
    if valor not in valores_unicos:
        valores_unicos.append(valor)

print("Lista sin elementos repetidos:", valores_unicos)

"""
5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
• Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
• Mostrar la lista final actualizada.
"""

estudiantes = ["Leo", "Victor", "Hugo", "Belen", "Mario", "Miguel", "Pepe", "Raul"]

opcion = input("¿Desea agregar (a) o eliminar (e) un estudiante?")
if opcion == "a":
    nuevo_estudiante = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo_estudiante)
elif opcion == "e":
    estudiante_a_eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    estudiantes.remove(estudiante_a_eliminar)
else:
    print("Opcion no válida.")

print("Lista final actualizada de estudiantes:", estudiantes)

"""
6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el
último pasa a ser el primero).
"""

numeros = [1, 2, 3, 4, 5, 6, 7]
print("Lista original:", numeros)

# Rotar a la derecha usando slicing
numeros = [numeros[-1]] + numeros[:-1] # Creo una nueva lista con el último elemento al frente y el resto despues

print("Lista rotada a la derecha:", numeros)

"""
7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una
semana.
• Calcular el promedio de las mínimas y el de las máximas.
• Mostrar en qué día se registró la mayor amplitud térmica.
"""

temperaturas = [
    [15, 25],  # Lunes
    [17, 28],  # Martes
    [14, 26],  # Miércoles
    [16, 30],  # Jueves
    [18, 27],  # Viernes
    [13, 24],  # Sábado
    [15, 29]   # Domingo
]

suma_minimas = 0
suma_maximas = 0

for i in range(7):
    suma_minimas += temperaturas[i][0]
    suma_maximas += temperaturas[i][1]

promedio_minimas = suma_minimas / 7
promedio_maximas = suma_maximas / 7
print("Promedio de temperaturas mínimas:", promedio_minimas)
print("Promedio de temperaturas máximas:", promedio_maximas)

# Calcular la amplitud térmica y el día correspondiente
amplitud_termica_max = 0
dia_amplitud_maxima = 0

for i in range(7):
    temp_min = temperaturas[i][0]
    temp_max = temperaturas[i][1]
    amplitud = temp_max - temp_min
    if amplitud > amplitud_termica_max:
        amplitud_termica_max = amplitud
        dia_amplitud_maxima = i

print("Dia con mayor amplitud:", dia_amplitud_maxima + 1)


"""
8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
• Mostrar el promedio de cada estudiante.
• Mostrar el promedio de cada materia
"""

notas = [
    [7, 8, 9],  # Estudiante 1
    [6, 7, 8],  # Estudiante 2
    [9, 9, 10], # Estudiante 3
    [5, 6, 7],  # Estudiante 4
    [8, 7, 6]   # Estudiante 5
]

# Promedio de cada estudiante
for i in range(5):
    suma_notas = 0
    for j in range(3):
        suma_notas += notas[i][j]
    promedio = suma_notas / 3
    print(f"Promedio del estudiante {i + 1}:", promedio)

# Promedio de cada materia
for j in range(3):
    suma_materia = 0
    for i in range(5):
        suma_materia += notas[i][j]
    promedio_materia = suma_materia / 5
    print(f"Promedio de la materia {j + 1}:", promedio_materia)

"""
9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
• Inicializarlo con guiones "-" representando casillas vacías.
• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
• Mostrar el tablero después de cada jugada
"""

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

jugador = "X"

while True:
    # Pido jugada al jugador
    fila= int(input(f"Jugador {jugador}, ingrese fila (1-2-3): ")) - 1
    columna= int(input(f"Jugador {jugador}, ingrese columna (1-2-3): ")) - 1

    # Coloco la jugada en el tablero
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Esa posicion ya esta ocupada")
        continue

    # Muestro el tablero actualizado
    for i in range(3):
        print(tablero[i])

    # Cambio de jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"


"""
10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
• Mostrar el total vendido por cada producto.
• Mostrar el día con mayores ventas totales.
• Indicar cuál fue el producto más vendido en la semana.
"""

ventas = [
    [10, 15, 20, 25, 130, 35, 40],  # Producto 1
    [5, 10, 15, 20, 25, 30, 35],   # Producto 2
    [8, 12, 16, 20, 24, 28, 32],   # Producto 3
    [7, 14, 21, 28, 35, 42, 49]    # Producto 4
]
producto_mas_vendido = None
producto_maximo = 0

# Total vendido por cada producto y producto mas vendido de la semana
for i in range(4):
    suma_producto = 0
    for j in range(7):
        suma_producto += ventas[i][j]

    print(f"El total vendido del producto {i+1} es: {suma_producto}")
    if suma_producto > producto_maximo:
        producto_maximo = suma_producto
        producto_mas_vendido = i

print(f"El producto mas vendido de la semana fue el {producto_mas_vendido + 1}")

# Dia con mayor ventas totales
dia_mayor_ventas = None
venta_maxima = 0

for d in range(7):
    suma_ventas_dia = 0 
    for p in range(4):
        suma_ventas_dia += ventas[p][d]
    print(f"La suma de ventas en el dia {d+1}: {suma_ventas_dia}")
    if suma_ventas_dia > venta_maxima:
        venta_maxima = suma_ventas_dia
        dia_mayor_ventas = d

print(f"El día con mayor ventas fue el {dia_mayor_ventas + 1}")
