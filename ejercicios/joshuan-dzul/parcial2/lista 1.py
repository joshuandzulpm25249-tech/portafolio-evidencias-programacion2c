#joshuan david dzul cohuo
"""
Trabajas en la organización de un evento de premios.
Tienes una lista de celebridades que entrarán por la alfombra roja. El orden es vital!
1. Crea una lista llamada invitados con los nombres: "Robert Downey Jr.", "Emma Stone" y "Cillian Murphy".
2. Llegada de último minuto. Agrega a "Zendaya" al final de la lista.
3. Invitado VIP: "Steven Spielberg" acaba de llegar y debe ir al principio de la lista.
4. Cancelación: "Emma Stone" avisa que no asistir.
5. seguridad El último de la lista se porta mal y debe ser retirado.
Imprime la lista final y cuántos quedan en total.
"""

#punto no1
invitados = ["robert dawny jr","emma stone","cillian murphy"]
#punto no2
invitados.append("zendaya")
#punto no3
invitados.insert(0,"steven spielberg")
#punto no4
invitados.remove("emma stone")
#punto no5
invitados.pop(3)
#punto no6
print(invitados,"no.total invitados: ",len(invitados))