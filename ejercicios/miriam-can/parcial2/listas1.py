"""
Trabajas en la organización de un evento de premios. Tienes una lista de
celebridades que entrarán por la alfombra roja. El orden es vital.
1. Crea una lista llamada invitados con los nombres: "Robert Downy Jr", 
"Emma Stone" y "Cillian Murphy"
2. Llegada de último minuto. Agrega a "Zendaya" al final de la lista.
3. Invitado VIP. "Steven Spielberg" acaba de llegar y debe ir al principio de
la lista
4. Cancelación. "Emma Stone" avisa que no podrá asistir.
5. Seguridad. El ultimo de la lista se portó mal y debe ser retirado
6. Imprime la lista final y cuantos invitados quedan en total.
"""

# punto no. 1
invitados = ["Robert Downy Jr","Emma Stone","Cillian Murphy"]
# punto no. 2
invitados.append("Zendaya")
# punto no. 3
invitados.insert(0,"Steven Spielberg")
# punto no. 4
#invitados.pop(2)
invitados.remove("Emma Stone")
# punto no. 5
invitados.pop(3) #invitados.pop() | del invitados[-1]
# punto no. 6
print(invitados,"No. total invitados: ",len(invitados))