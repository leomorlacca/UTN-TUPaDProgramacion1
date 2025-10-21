"""1) Dado el diccionario precios_frutas
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""

frutas = list(precios_frutas.keys())

print(frutas)

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe
"""

agenda_telefonica = {}
for _ in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número telefónico: ")
    agenda_telefonica[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto que desea mostrar el numero: ")
if nombre_consulta in agenda_telefonica:
    print(f"El número de {nombre_consulta} es {agenda_telefonica[nombre_consulta]}")
else:
    print(f"No existe un contacto con el nombre {nombre_consulta}")

"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

frase = input("Ingrese una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras unicas:", palabras_unicas)

"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""
alumno1 = input("Ingrese el nombre del primer alumno: ")
notas1 = []
for i in range(3):
    notas1.append(float(input(f"Ingrese la nota {i+1} del alumno {alumno1}: ")))
notas1 = tuple(notas1)

alumno2 = input("Ingrese el nombre del segundo alumno: ")
notas2 = []
for i in range(3):
    notas2.append(float(input(f"Ingrese la nota {i+1} del alumno {alumno2}: ")))
notas2 = tuple(notas2)
               
alumno3 = input("Ingrese el nombre del tercer alumno: ")
notas3 = []
for i in range(3):
    notas3.append(float(input(f"Ingrese la nota {i+1} del alumno {alumno3}: ")))
notas3 = tuple(notas3)

promedio1 = sum(notas1) / len(notas1)
promedio2 = sum(notas2) / len(notas2)
promedio3 = sum(notas3) / len(notas3)

print(f"El promedio de {alumno1} es {promedio1}")
print(f"El promedio de {alumno2} es {promedio2}")
print(f"El promedio de {alumno3} es {promedio3}")

"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
"""

aprobados_parcial_1 = {"Juan", "Leo", "Pepe"}
aprobados_parcial_2 = {"Leo", "Ana", "Juan"}

ambos_parciales = aprobados_parcial_1.intersection(aprobados_parcial_2)
solo_un_parcial = aprobados_parcial_1.symmetric_difference(aprobados_parcial_2)
al_menos_un_parcial = aprobados_parcial_1.union(aprobados_parcial_2)

print("Aprobaron ambos parciales:", ambos_parciales)
print("Aprobaron solo uno de los dos parciales:", solo_un_parcial)
print("Aprobaron al menos un parcial:", al_menos_un_parcial)

"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

stock_productos = {}
while True:
    accion = input("Ingrese 'C' para consultar stock, 'A' para agregar unidades, 'N' para agregar un nuevo producto o 'salir' para terminar: ").lower()
    if accion == 'salir':
        break
    elif accion == 'C':
        producto = input("Ingrese el nombre del producto a consultar: ")
        if producto in stock_productos:
            print(f"El stock de {producto} es {stock_productos[producto]}")
        else:
            print(f"No existe el producto {producto} en el stock.")
    elif accion == 'A':
        producto = input("Ingrese el nombre del producto al que desea agregar unidades: ")
        if producto in stock_productos:
            unidades = int(input(f"Ingrese la cantidad de unidades a agregar al stock de {producto}: "))
            stock_productos[producto] += unidades
            print(f"El nuevo stock de {producto} es {stock_productos[producto]}")
        else:
            print(f"No hay {producto} en stock.")
    elif accion == 'N':
        producto = input("Ingrese el nombre del nuevo producto: ")
        if producto not in stock_productos:
            unidades = int(input(f"Ingrese la cantidad inicial de unidades para {producto}: "))
            stock_productos[producto] = unidades
            print(f"{producto} agregado - {unidades} unidades")
        else:
            print(f"{producto} ya existe en el stock.")
    else:
        print("Opcion invalida. Por favor, intente nuevamente.")

"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora
"""



"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""