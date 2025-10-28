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