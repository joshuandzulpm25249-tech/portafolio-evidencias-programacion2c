"""Trabajas en la organización de un evento de premios. Tienes una lista de celebridades que entraran por la alfombra roja.El orden es vital. 
1. Crea una lista llamada invitados con los nombres:"robert downy jr","emma stone" y "cillian murphy"
2. Llegando de último minuto. Agrega a "zendaya" al final de la lista.
3. Invitado IVP. "steren spielberg" acaba de llegar y debe ir al principio de la lista.
4. Cancelación. "emma stone" avisa que no podra asistir .
5. Seguridad. El último de la lista se porto mal y debe ser retirado.
6. Imprime la lista final y cuantos imvitados quedan en total"""

#punto no.1
invitados=["robert downy jr","emma stone","cillian murphy"]
#punto no.2
invitados.append("zendaya")
#punto no.3
invitados.insert(0,"steven spielberg")
#punto no.4
invitados.remove("emma stone")
#punto no.5
invitados.pop(3) 
#punto no.6
print(invitados,"no. total invitados: ",len(invitados))
