#jose miguel 

productos = ["leche","pan","huevo","manzana"]
#prouctos nuevos = ["arroz","frijol","aceite"]
#producto.extend(ProductosNuevos)
productos.extend(["arroz","frijol","aceite"])
productos.pop(productos.index("pan"))
productos.sort()
print(productos)
if "leche" in productos:
    print("si tenemos leche")
else:
    print("no tenemos leche")