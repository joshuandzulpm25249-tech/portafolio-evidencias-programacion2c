"""Estas programando el sistema de una pequeña tienda,debes manipular el inventario de productos disponibles
1.Inicia una lista de productos que contenga: "leche","pan","huevos","manzanas",
2.Te ha llegado un camion con nuevos productos: "Arroz","Frijol" y "Aceite".Agregalos todos a la lista usando un solo metodo
3.Te das cuenta que el "pan" esta vencido.Encuentra el indice del "pan" usando .index() y luego eliminalo de la lista
4.El dueño quiere que la lista se vea profesional.usa el metodo sort()para ordenar los productos.
5.El cliente pregunta si hay "leche".Usa el operador in para imprimir un mensaje que diga "Si,tenemos leche"
o "No disponible"."""


productos = ["leche","pan","huevos","manzanas",]
productos.extend(["Arroz","frijol","aceite"])
productos.sort()
print(productos)
if "leche" in productos:
    print("si,tenemos leche")
else:
    print("no disponible")