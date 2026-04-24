#Raul Haas Pool
#Estamos programando  el sistema de una pequeña tienda, debes manipular tu inventario de productos disponibles.
#1. Inicia una lista de productos que contenga "Leche", "Pan", "Huevos", "Manzana".
#2. Te ha llegado un camion con nuevos productos "Arroz", "Frijol" y "Aceite". Agregalos todos a la lista usando
#un solo metodo.
#3. Te das cuenta que el "Pan" esta vencido. Encuentra el indice del "Pan" usando .index() luego eliminalo de la lista.
#4. El dueño quiere que la lista se vea profesional usando el metodo sort() para ordenar los productos.
#5. El cliente pregunta si hay "Leche". Usa el operador in para imprimir un mensaje que diga. "Si, tenemos leche" o 
#"No disponibles".

productos = ["Leche", "Pan", "Huevos", "Manzanas"]
productos.extend(["Arroz", "Frijol", "Aceite"])
productos.pop(productos.index("Pan"))
productos.sort()
print(productos)
if "Leche" in productos:
    print("Si, tenemos leche")
else:
    print("No disponible")    
