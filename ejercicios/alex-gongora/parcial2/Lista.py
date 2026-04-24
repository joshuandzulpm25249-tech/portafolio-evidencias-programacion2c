"""
Trabajas en la organización de un evento de premios.
Tienes una lista de celebridades que entrarán por la alfombra roja. El orden es vital!
1. Crea una lista llamada invitados con los nombres: "Robert Downey Jr.", "Emma Stone" y "Cillian Murphy".
2. Llegada de último minuto. Agrega a "Zendaya" al final de la lista.
3. Invitado VIP: "Steven Spielberg" acaba de llegar y debe ir al principio de la lista.
4. Cancelación: "Emma Stone" avisa que no asistirá por seguridad. El último de la lista se porta mal y debe ser retirado.
5. Imprime la lista final y cuántos quedan en total.
"""

#Alexander Gongora
#lista 

#Punto 1
Invitados= ["Robert Downy Jr", "Emma Stone", "cillian Murphy"]
#Punto 2 
Invitados.append("Zendaya")
#Punto 3 
Invitados.insert(0, "Steven Spielberg")
#Punto 4
#Invitados.pop(2)
Invitados.remove("Emma Stone")
#Punto 5 
Invitados.pop(3)
#Puntos 6
print(Invitados, "No. total invitados: ", len(Invitados))