#joshuan david dzul cohuo
"""""
estas programando el sistema de una pequeña tienda debes manipular el inventario de productos disponibles
1.-Te ha llegado un camión con muevos productos"arroz","frijol","aceite".Agregalos todos a la lista usando un solo metodo.
2.-Te ha dedo cuenta que el "pan" esta vencido .Encuentra el indice del "pan" usando index()y lluegp eliminalo de la lista.
3.-
"""""
productos = ["leche","pan","huevos","manzanas"]
productos.extend(["arroz","frijol","aceite"])
productos.pop(productos.index("pan"))
productos.sort()
print(productos)
if"leche"in productos:
    print("si tenemosleche")
else:
    print("no disponible")