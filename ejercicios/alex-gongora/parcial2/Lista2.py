"""
Estás Programando el sistema de una pequeña tienda. Debes manipular el inventario de Productos disponibles:
1. Inicia una lista de Productos que contengan: "Leche", "Pan", "Huevos", "Manzanas".
2. Te ha llegado un camión nuevo de Productos: "Arroz", "Frijol" y "Aceite". Agregalos todos a la lista usando solo método.
3. Te das cuenta que el "Pan" está vencido. Encuentra el índice del "Pan" usando .index() y luego elimínalo de la lista.
4. El dueño quiere que se vea profesional. Usa el método sort() para ordenar los Productos.
5. El Cliente pregunta si hay "Leche". Usa el operador in para imprimir un mensaje que diga "Sí, tenemos leche" o "No disponible".
"""

#Alexander Gongora
#Lista 2 

productos=["Leche", "Pan", "Huevos", "Manzana"]
productos.extend(["Arroz", "Frijol", "Aceite"])
productos.pop(productos.index("Pan"))  #Producto 1
productos.sort()
print(productos)
if "Leche" in productos:
    print("Si, tenemos leche")
else:
    print("No, disponible")