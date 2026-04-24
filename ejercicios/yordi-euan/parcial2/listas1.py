""" trabajas en la organizacion de un evento de premios.Tienes una lista de celebridades que entraran por la alfombra roja.El orden es vital.
1. crea una lista llamada invitados con los nombres: "Robert Downey Jr","Emma Stone",y "Cillian Murphy" 
2. Llegada de ultimo momento.Agrega a "Zendaya" al final de la lista
3. Invitado VIP."Steven Spielberg"acaba de llegar y debe ir al principio de la lista
4. Cancelacion."Emma Stone"avisa que no podra asisistir.
5. Seguridad. El ultimo de la lista se porto mal y debe ser retirado
6. Imprime la lista al final y cuantos invitados quedan en total."""

#Punto no.1
invitados = ["Robert Downy Jr","Emma Stone","Cillion Murphy"]
#Punto no.2
invitados.append("Zendaya")
#punto no.3
invitados.insert(0,"Steven Spielberg")
#Punto no.4
invitados.pop(2) 
#punto no.5
invitados.pop(3)
#Punto no.6
print(invitados,"no.Total invitados: ", len(invitados))