"""estas programando el sistema de una pequeña tienda y 
debes manipular el inventario de productos disponibles.

1 inicia una lista de productos que contenga "leche","pan","huevo","manzana"
2 te a llegado un camion con productos. "aroz","frijol" y "aceite".
agregalos todos ala lista usando un solo metodo.
3 tedas cuenta que el "pan"esta vencido. 
Encuentra el indice del "pan" usando .index()y luego elimina lo de la lista.
4 el señor quiere que la lista se vea profecional usa el metoda sort()para ordenar los productos.
5 elcliente pregunta si hay "leche".usa el operadoe in para imprimir un mensage que diga "si, tenemos leche"
o "no desponible"."""
productos=["leche","pan","huevo","manzana"]
productos.extend(["aroz","frijol","aceite"])
productos.pop(productos.index("pan"))
productos.sort()
print(productos)
if "leche" in productos:
    print("si,tenemos leche")
else:
    print("No disponible")