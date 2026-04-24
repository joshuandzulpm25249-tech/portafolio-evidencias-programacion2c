#Alexa Cristel Ake Cuevas
#Estas programando el sistema de una pequeña tienda.Debes manipular el inventaeio de productos disponibles 
#1.Inicia una lista de productos que contega:"leche","pan","huevos","manzana"
#2.Te ha llegado un camion con nuevos productos:"arroz","frijol","aceite".Agregalos todo a la lista usando un solo metodo.
#3.Te das cuenta que el "pan" esta vencido.Encuentra el indice del "pan" usando.index() y luego eliminalo de la lista 
#4.El dueño quiere la lista se vea profesinal .usa el metodo sert() para ordenar los productos
#5.El cliente pregunta si hya leche.usa el operador in para imprimir un mensaje que diga "si,tenemos leche" o "no disponible"

productos = ("leche","pan","huevos","manzanas")
productos.extend(["Arroz","Frijol","Aceite"])
productos.pop(productos.index("pan"))
productos.sort()
print(productos)
if "Leche" in productos:
    print("si , tenemos leche")
else:
    print("no disponible")
    