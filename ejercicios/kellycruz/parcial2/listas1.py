#Kelly Juliet Cruz Torres
#trabaja en la organizacion de un evento de precios. Tienes una lista de celebridades.
#1.Crea una lista llamada invitados con los nombres:"roberto downy jr","emma stone","cillian murphy"
#2.llegada de ultimo momento.Agrega a  "zendaya" al final de la lista
#3.invitado VIP ."steven spleder" acaba de llegar y debe de ir al principio de la lista
#4.cancelacion."Emma stone" aviso que no podra asistir 
#5.seguridad.El ultimo de la lista se porto mal y debe ser retirado
#6imprime la lista final y cuantos invitados queda en la lista 

#punto no.1
invitados= ["roberto downy jr","emma stone","cillian murphy"]
#punto no.2
invitados.append("zendaya")
#punto no.3
invitados.insert(0,"steven sprelber")
#punto no.4
#invitados.pop(2)
invitados.remove("emma stone")
#punto no.5
invitados.pop(3)
#punto no.6
print(invitados,"No total invitados: ",len(invitados))