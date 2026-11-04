def filtrar_urgentes(tickets):
    urgentes = []
    for ticket in tickets:
        if ticket["prioridad"] == "alta":
            urgentes.append(ticket)
    return urgentes

tickets = [
    {"cliente": "Ana", "prioridad": "alta"},
    {"cliente": "Luis", "prioridad": "baja"},
    {"cliente": "Marta", "prioridad": "alta"},
]

print(filtrar_urgentes(tickets))

def buscar_cliente(tickets, nombre):
    for ticket in tickets:
        if ticket["cliente"] == nombre:
            return ticket
    return None

print(buscar_cliente(tickets, "Marta"))
print(buscar_cliente(tickets, "Pedro"))

tickets_por_cliente = {
    "Ana": {"prioridad": "alta"},
    "Luis": {"prioridad": "baja"},
    "Marta": {"prioridad": "alta"},
}

print(tickets_por_cliente["Marta"])
print(tickets_por_cliente.get("Pedro"))

def contar_altas(tickets):
    count = 0
    for ticket in tickets:
        if ticket["prioridad"] == "alta":
            count += 1
    return count

print(contar_altas(tickets))

def clientes_baja(tickets):
    nombres = []
    for ticket in tickets:
        if ticket["prioridad"] == "baja":
            nombres.append(ticket["cliente"])
    return nombres

print(clientes_baja(tickets))

def contar_vocales(texto):
    contador = 0
    for letra in texto.lower():
        if letra in "aeiou":
            contador += 1
    return contador

print(contar_vocales("Buenos Aires"))

def invertir(texto):
    resultado = ""
    for letra in texto:
        resultado = letra + resultado
    return resultado

print(invertir("AFTR"))

palabra = "AFTR"
print(palabra[0:2])    # AF  (positions 0 and 1)
print(palabra[::2])    # AT  (every second letter)
print(palabra[::-1])   # RTFA (backwards)


def precio_maximo(precios):
    maximo = precios[0]
    for precio in precios:
        if precio > maximo:
            maximo = precio
    return maximo

precios = [10000, 35000, 12000, 40000, 30000]
print(precio_maximo(precios))

print(max(precios))
print(sorted(precios))
print(sorted(precios, reverse=True))

productos = [
    {"nombre": "Remera", "precio": 10000},
    {"nombre": "Pantalón", "precio": 35000},
    {"nombre": "Buzo", "precio": 30000},
]

ordenados = sorted(productos, key=lambda p: p["precio"], reverse=True)
for p in ordenados:
    print(p["nombre"], p["precio"])

def contar_letra(texto, letra):
    contador = 0
    for caracter in texto.lower():
        if caracter == letra:
            contador += 1
    return contador

print(contar_letra("Buenos Aires", "e"))