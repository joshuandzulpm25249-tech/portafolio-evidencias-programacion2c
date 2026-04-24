"""Estas programando el sistema de una pequeña tienda. Debes manipular el inventario de productos disponibles.
1. Inicia una lista de productos que contenga: "leche","pan","huevos","manzanas"
2. Te ah llegado un camión con nuevos productos:"arroz","frijol" y "aceite". Agregalos todo a la lista usando un solo metodo.
3. Te das cuenta que el "pan" esta vencido. Encuentra el indice del "pan" usando .index() y luego eliminalo de la lista.
4. El dueño quiere que la lista se vea profesional. Usa el metodo sar() para ordenar los productos.
5. El cliente pregunta si hay "leche", usa el operador in para imprimir un mensaje que diga "si, tenemos leche" o "no disponible"""

productos =["leche","pan","huevos","manzanas"]
productos.extend(["arroz","frijol","aceite"])
productos.pop(productos.index("pan")) 
productos.sort()
print(productos)
if "leche" in productos:
    print("si, tenemos leche")
else:
    print("no disponible")