#Perla Cristel Couoh Terat
#Estas programando el sistema de una pequeña tienda. Debes manipular el inventario de productos disponibles.

#1Inicia una lista de productos que contenga: "Leche", "Pan", "Huevos", "Manzana".
#2Te ha llegado un camion con nuevos productos: "Arroz", "Frijol" y "Aceite". Agregalos todos a la lista usando un solo metodo.
#3Te das cuenta que el "Pan" esta vencido. Encuentra el indice del "Pan" usando .index() y luego eliminalo de la lista
#4El dueño quiere que la lista se vea profesional. Usa el metodo sort() para ordenar los productos.
#5El cliente pregunta si hay "Leche". Usa el operador in para umprimir un mensaje que diga "Si, tenemos leche" o "No disponible"
productos = ("Leche", "Pan", "Huevos", "Manzanas")
productos.extend(["Arroz", "Frijol", "Aceite"])
productos.pop(productos.index("Pan"))
productos.sort()
print(productos)
if "Leche" in productos:
    print("Si, tenemos leche")
else:
    print("No disponible")
