"""
Estas programano el sistema de una pequeña tienda. Debes manipular el inventario
de productos disponibles.
1. Inicia una lista de productos que contenga: "Leche", "Pan", "Huevos", "Manzanas"
2. Te ha llegado un camion con nuevos productos: "Arroz", "Frijol" y "Aceite".
Agregalos todos a la lista usando un solo método.
3. Te das cuenta que el "Pan" esta vencido. Encuentra el indice del "Pan" usando
.index() y luego elimínalo de la lista.
4. El dueño quiere que la lista se vea profesional. Usa el metodo sort() para
ordenar los productos.
5. El cliente pregunta si hay "Leche". Usa el operador in para imprimir un
mensaje que diga "Si, tenemos leche" o "No disponible".
"""
productos = ["Leche","Pan","Huevos","Manzanas"]
#productosNuevos = ["Arroz", "Frijol", "Aceite"]
#productos.extend(productosNuevos)
productos.extend(["Arroz","Frijol","Aceite"])
productos.pop(productos.index("Pan")) #productos.pop(1)
productos.sort()
print(productos)
if "Pan" in productos:
    print("Si, tenemos leche")
else:
    print("No disponible")