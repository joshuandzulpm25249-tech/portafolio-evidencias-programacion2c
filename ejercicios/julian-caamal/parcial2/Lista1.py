"""trabajas en la organisacion de un evento de premios,Tienes una lista de selebridades
que entraran por la alfombra roja. el ordem es vital
1 crea una lista llamada 
invitados con los nombres:"robert downt jr","emma stone" y "cillian murphy"
2 llegada de ultimo minuto.Agrega a "zenday" al final de la lista.
3 invitado VIP."steven spielber" acaba de llegar y debe ir al principio de la lista.
4 cancelacion."emma stone" avisa que no podra asistir.
5 seguridad.El ultimo de la lista se porto mal y debe ser retrado.
6 imprime la lista final y cuantos invitados quedan en total"""

#punto no.1
invitados=["robert downt jr","emma stone","cillian murphy"]
#punto no.2
invitados.append("zenday")
#punto no.3
invitados.insert(0,"steven spielber")
#punto no.4
invitados.remove("emma stone")
#punto no.5
invitados.pop(3)
#punto no.6
print(invitados,"no. total invitados: ",len(invitados))