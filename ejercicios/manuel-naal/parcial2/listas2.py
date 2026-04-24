productos = ["leche","pan","huevos","manzanas"]
#productosNuevos =["arroz","frijol";"aceite"]
productos.extend(["arroz","frijol","aceite"])
productos.pop(productos.index("pan")) #productos.pop(1)
productos.sort()
print(productos)
if "leche" in productos:
    print("Si, tenemos leche")
else:
    print("No disponible")
