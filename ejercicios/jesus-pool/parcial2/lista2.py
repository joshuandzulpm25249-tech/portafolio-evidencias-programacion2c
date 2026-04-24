"""
Estás Programando el sistema de una pequeña tienda. Debes manipular el inventario de Productos disponibles:
1. Inicia una lista de Productos que contengan: "Leche", "Pan", "Huevos", "Manzanas".
2. Te ha llegado un camión nuevo de Productos: "Arroz", "Frijol" y "Aceite". Agregalos todos a la lista usando solo método.
3. Te das cuenta que el "Pan" está vencido. Encuentr a el índice del "Pan" usando .index() y luego elimínalo de la lista.
4. El dueño quiere que se vea profesional. Usa el método sort() para ordenar los Productos.
5. El Cliente pregunta si hay "Leche". Usa el operador in para imprimir un mensaje que diga "Sí, tenemos leche" o "No disponible".
"""


productos = ["leche", "pan", "huevos", "manzanas"]


# Nuevos productos que llegaron
productos_nuevos = ["arroz", "frijol", "aceite"]


# Agregar todos los nuevos productos a la lista
productos.extend(productos_nuevos)


# Eliminar "pan" (producto vencido)
indice_pan = productos.index("pan")
productos.pop(indice_pan)


# Ordenar la lista
productos.sort()


# Mostrar la lista final
print(productos)


# Verificar si hay leche
if "leche" in productos:
   print("Sí, tenemos leche")
else:
   print("No disponible")


