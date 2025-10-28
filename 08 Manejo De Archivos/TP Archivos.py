"""
1) Crear un archivo de texto llamado "productos.txt" que contenga una lista de productos, cada uno con su nombre, 
    precio y cantidad, separados por comas.
"""
def crear_archivo_productos():
    with open("productos.txt", "w") as archivo:
        archivo.write("mouse,6000,3\n")
        archivo.write("teclado,8500,4\n")
        archivo.write("monitor,140000,2\n")
    print("Archivo 'productos.txt' creado con éxito.")

crear_archivo_productos()

"""
2) Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada
línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente
formato:
Producto: Lapicera | Precio: $120.5 | Cantidad: 30
"""

def mostrar_productos():
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            nombre, precio, cantidad = linea.split(",")
            print(f"Producto: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")

mostrar_productos()

"""
3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar
los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio,
cantidad) y lo agregue al archivo sin borrar el contenido existente.
"""

def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = input("Ingrese el precio del producto: ")
    cantidad = input("Ingrese la cantidad del producto: ")
    
    with open("productos.txt", "a") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")
    print(f"Producto agregado con éxito.")

agregar_producto()

"""
4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en
una lista llamada productos, donde cada elemento sea un diccionario con claves:
nombre, precio, cantidad.
"""

def cargar_productos_en_lista():
    productos = []
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            nombre, precio, cantidad = linea.split(",")
            producto = {
                "nombre": nombre,
                "precio": float(precio),
                "cantidad": int(cantidad)
            }
            productos.append(producto)
    return productos

productos = cargar_productos_en_lista()
print(productos)

"""
5. Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un
producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si
no existe, mostrar un mensaje de error.
"""

def buscar_producto(producto):
    encontrado = False
    with open("productos.txt", "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            nombre, precio, cantidad = linea.split(",")
            if nombre.lower() == producto.lower():
                print(f"Producto encontrado: Nombre: {nombre} | Precio: ${precio} | Cantidad: {cantidad}")
                encontrado = True
                break
    if not encontrado:
        print(f"El producto '{producto}' no existe en el archivo.")

producto_a_buscar = input("Ingrese el nombre del producto a buscar: ")
buscar_producto(producto_a_buscar)

"""
6. Guardar los productos actualizados: Después de haber leído, buscado o agregado
productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los
productos actualizados desde la lista.
"""

def guardar_productos_en_archivo(productos, ruta="productos.txt"):
    with open(ruta, "w") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print(f"Archivo actualizado.")

# en cada operacion que modifique la lista de productos, llamar a esta funcion
# guardar_productos_en_archivo(productos)