#Raul Haas Pool
#Trabajas en la organizacion de un evento de premios. Tienes una lista de celebridades que entraran 
#por la alfombra roja. El orden es vital.
#1. Crea una lista llamada invitados con los nombres: "Robert Downy Jr", "Emma Stone", "Cillian Murphy".
#2. Llegada de ultimo minuto. Agrega a "Zendaya" al final de la lista.
#3. Invitado VIP "Steven Sprielber" acaba de llegar y debe ir al principio de la lista.
#4. Cancelacion. "Emma Stone" avisa que no podra estar.
#5. Seguridad. El ultimo de la lista se porto mal y debe ser retirado.
#6. Imprime la lista final y cuantos invitados quedan en total.

#Punto no.1
invitados = ["Robert Downy Jr", "Emma Stone", "Cillian Murphy"]

#Punto no.2
invitados.append("Zendaya")

#Punto no.3
invitados.insert(0, "Steven Sprielber")

#Punto no.4
invitados.remove("Emma Stone")

#Punto no.5
invitados.pop(3)

#Punto no.6
print(invitados, "No. total invitados:", len(invitados))