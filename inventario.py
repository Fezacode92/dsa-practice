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

def reponer(inventario, producto, cantidad):
    if producto not in inventario:
        print(f"{producto} no existe")
        return
    inventario[producto]["stock"] += cantidad
    print(f"Repuesto: {cantidad} x {producto}")

def stock_bajo(inventario, minimo=5):
    alertas = []
    for nombre, datos in inventario.items():
        if datos["stock"] <= minimo:
            alertas.append(nombre)
    return alertas

vender(inventario, "buzo_oversize", 2)
vender(inventario, "buzo_oversize", 5)
reponer(inventario, "remera_negra", 10)
mostrar_inventario(inventario)
print("Reponer:", stock_bajo(inventario))