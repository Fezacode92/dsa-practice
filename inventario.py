import json

inventario = {
    "remera_negra": {"precio": 10000, "stock": 10},
    "pantalon_cargo": {"precio": 35000, "stock": 5},
    "buzo_oversize": {"precio": 30000, "stock": 3},
}

def mostrar_inventario(inventario):
    for nombre, datos in inventario.items():
        print(f"{nombre}: ${datos['precio']} - {datos['stock']} unidades")

def vender(inventario, producto, cantidad):
    if producto not in inventario:
        print(f"{producto} no existe")
        return
    if inventario[producto]["stock"] < cantidad:
        print(f"No hay suficiente stock de {producto}")
        return
    inventario[producto]["stock"] -= cantidad
    print(f"Vendido: {cantidad} x {producto}")
    guardar_inventario(inventario)

def reponer(inventario, producto, cantidad):
    if producto not in inventario:
        print(f"{producto} no existe")
        return
    inventario[producto]["stock"] += cantidad
    print(f"Repuesto: {cantidad} x {producto}")
    guardar_inventario(inventario)

def agregar_producto(inventario, producto, precio, stock):
    if producto in inventario:
        print(f"{producto} ya existe")
        return
    inventario[producto] = {"precio": precio, "stock": stock}
    print(f"Agregado: {producto}")
    guardar_inventario(inventario)    

def stock_bajo(inventario, minimo=5):
    alertas = []
    for nombre, datos in inventario.items():
        if datos["stock"] <= minimo:
            alertas.append(nombre)
    return alertas

def guardar_inventario(inventario, archivo="inventario.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump(inventario, f, indent=4, ensure_ascii=False)
    print("Inventario guardado")

def cargar_inventario(archivo="inventario.json"):
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("No hay archivo, usando inventario inicial")
        return inventario

inventario = cargar_inventario()

while True:
    print("\n1. Ver inventario")
    print("2. Vender")
    print("3. Reponer")
    print("4. Salir")
    print("5. Agregar producto")
    opcion = input("Elegí una opción: ")

    if opcion == "1":
        mostrar_inventario(inventario)
    elif opcion == "2":
        producto = input("Producto: ").lower().strip()
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("La cantidad tiene que ser un número")
            continue
        vender(inventario, producto, cantidad)
    elif opcion == "3":
        producto = input("Producto: ").lower().strip()
        try:
            cantidad = int(input("Cantidad: "))
        except ValueError:
            print("La cantidad tiene que ser un número")
            continue
        reponer(inventario, producto, cantidad)
        mostrar_inventario(inventario)
    elif opcion == "4":
        print("Chau!")
        break
    elif opcion == "5":
        producto = input("Producto: ").lower().strip()
        try:
            precio = float(input("Precio: "))
            stock = int(input("Stock: "))
        except ValueError:
            print("El precio y el stock tienen que ser números")
            continue
        agregar_producto(inventario, producto, precio, stock)
    else:
        print("Opción no válida")