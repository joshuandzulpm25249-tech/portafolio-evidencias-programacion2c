#Perla Cristel Couoh Terat
#Trabajas en la organización de un evento de premios. Tienes una lista de celebridades que entraran por la alfombra roja. El orden es vital.
#1Crea una lista llamada invitados con los nombres: "Robert Downy Jr","Emma Stone" y "Cillian Murphy".
#2Llegada de ultimo minuto. Agrega a "Zendaya" al final de la lista
#3Invitado VIP. "Steven Sprelber" acaba de llegar y debe de ir al principio de la lista.
#4Cancelación "Emma Stone" avisa que no podra asistir.
#5Seguridad. El ultimo de la lista se porto mal y debe de ser retirado.
#6Imprime la lista final y cuantos invitados quedan en total.

#Punto no.1 
invitados = ["Robert Downy Jr", "Emma Stone", "Cillian Murphy"]
#Punto no.2
invitados.append("Zendaya")
#Punto no.3
invitados.insert(0,"Steven Sprelber")
#Punto no.4
#invitados.pop(2)
invitados.remove("Emma Stone")
#Punto no.5
invitados.pop (3)
#Punto no.6
print(invitados, "No. total invitados: ", len(invitados))