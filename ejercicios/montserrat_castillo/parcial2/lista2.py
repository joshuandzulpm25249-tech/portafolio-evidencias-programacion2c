#Montserrat Castillo

productos = ["Leche","Pan","Huevo","Manzana"]
#productosNuevos = ["arroz","frijol","aceite"]
#productos.extend(productosNuevos)
productos.extend(["arroz","frijol","aceite"])
productos.pop(productos.index("Pan"))
productos.sort()
print(productos)
if "leche" in productos:
    print("si, tenemos leche")
else:
    print("No tenemos leche")