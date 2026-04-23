productos = ["leche", "pan", "huevos", "manzanas"]
productos_nuevos = ("Arroz", "Frijol", "Aceite")
productos.extend(productos_nuevos)
productos.pop(productos.index("pan"))
productos.sort()
print(productos)

if "leche" in productos:
    print("si, tenemos leche")
else:
    print("no tenemos leche")