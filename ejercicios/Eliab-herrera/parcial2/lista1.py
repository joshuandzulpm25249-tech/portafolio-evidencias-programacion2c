#Trabajas en la organización de un evento de premios.
#Tienes una lista de celebridades que entrarán por la alfombra roja. El orden es vital!
#1. Crea una lista llamada invitados con los nombres: "Robert Downey Jr.", "Emma Stone" y "Cillian Murphy".
#2. Llegada de último minuto. Agrega a "Zendaya" al final de la lista.
#3. Invitado VIP: "Steven Spielberg" acaba de llegar y debe ir al principio de la lista.
#4. Cancelación: "Emma Stone" avisa que no asistirá por seguridad. El último de la lista se porta mal y debe ser retirado.
#5. Imprime la lista final y cuántos quedan en total.

#Eliab israel herrera naal
#lista1
invitados = ["robert downy jr","Emma stone","cillan murphy"]
invitados.append("zendaya")
invitados.insert(0,"stevan spielberg")
invitados.remove("Emma stone")
invitados.pop(3)
print(invitados,"no,total,invitados:",len(invitados))