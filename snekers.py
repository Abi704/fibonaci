# Definimos la base de datos como una lista vacía
print("Comercial de Sneakers - Gestión de productos")
base_de_datos = []

# Contraseña predefinida
CONTRASENA = "sneaker123"

# Función para solicitar contraseña
def verificar_contraseña():
    intento = input("Ingrese la contraseña para acceder: ")
    if intento == CONTRASENA:
        print("Contraseña correcta.\n")
        return True
    else:
        print("Contraseña incorrecta. Intente nuevamente.\n")
        return False

# Función para agregar un nuevo producto
def agregar_producto():
    print("Agregar nuevo producto")
    codigo_producto = input("Código del producto (ej. SNK001): ")
    modelo = input("Modelo: ")
    marca = input("Marca: ")
    talla = input("Talla (ej. 42, 43, etc.): ")
    color = input("Color: ")
    temporada = input("Temporada (Verano, Invierno, etc.): ")
    cantidad = int(input("Cantidad en stock: "))
    material = input("Material: ")
    tipo_suela = input("Tipo de suela (ej. goma, caucho, etc.): ")
    estilo = input("Estilo (ej. deportivo, casual, etc.): ")
    
    # Agregar el producto como un diccionario a la base de datos
    producto = {
        "codigo_producto": codigo_producto,
        "modelo": modelo,
        "marca": marca,
        "talla": talla,
        "color": color,
        "temporada": temporada,
        "cantidad": cantidad,
        "material": material,
        "tipo_suela": tipo_suela,
        "estilo": estilo
    }
    
    base_de_datos.append(producto)
    print("Producto agregado exitosamente.\n")

# Función para consultar (mostrar) los productos
def consultar_productos():
    if not base_de_datos:
        print("No hay productos en la base de datos.\n")
    else:
        for producto in base_de_datos:
            print("===================================")
            for clave, valor in producto.items():
                print(f"{clave.capitalize()}: {valor}")
            print("===================================")
        print("\n")

# Función para modificar un producto
def modificar_producto():
    codigo = input("Ingrese el código del producto a modificar: ")
    encontrado = False
    
    for producto in base_de_datos:
        if producto["codigo_producto"] == codigo:
            print("Producto encontrado. ¿Qué deseas modificar?")
            producto["modelo"] = input(f"Nuevo modelo (actual: {producto['modelo']}): ")
            producto["marca"] = input(f"Marca (actual: {producto['marca']}): ")
            producto["talla"] = input(f"Talla (actual: {producto['talla']}): ")
            producto["color"] = input(f"Color (actual: {producto['color']}): ")
            producto["temporada"] = input(f"Temporada (actual: {producto['temporada']}): ")
            producto["cantidad"] = int(input(f"Cantidad (actual: {producto['cantidad']}): "))
            producto["material"] = input(f"Material (actual: {producto['material']}): ")
            producto["tipo_suela"] = input(f"Tipo de suela (actual: {producto['tipo_suela']}): ")
            producto["estilo"] = input(f"Estilo (actual: {producto['estilo']}): ")

            print("Producto modificado exitosamente.\n")
            encontrado = True
            break
    
    if not encontrado:
        print("Producto no encontrado.\n")

# Función para eliminar un producto
def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    encontrado = False
    
    for i, producto in enumerate(base_de_datos):
        if producto["codigo_producto"] == codigo:
            del base_de_datos[i]
            print("Producto eliminado exitosamente.\n")
            encontrado = True
            break
    
    if not encontrado:
        print("Producto no encontrado.\n")

# Función principal del programa
def menu():
    while True:
        print("Menú de opciones:")
        print("1. Agregar producto (Alta)")
        print("2. Consultar productos (Mostrar)")
        print("3. Modificar producto (Editar)")
        print("4. Eliminar producto (Borrar)")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            consultar_productos()
        elif opcion == "3":
            modificar_producto()
        elif opcion == "4":
            eliminar_producto()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.\n")

# Ejecución del programa
if verificar_contraseña():
    menu()
