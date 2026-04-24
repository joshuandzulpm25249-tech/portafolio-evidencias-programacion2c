#Alexa Cristel Ake Cuevas
#Trabaja en la organizaciuon de un evento de precios.Tienes una lista de celenbridades que contaran por la alfrombra roja.El orden es vital
#1.Crea una lista llamada invitados con los nombres:"Roberto Downy Jr","Emma stone "y  "cillian morphy"
#2. Llegada de ultimo momento.Agrega a "zendaya" al final de la lista
#3.Invitado VIP."stven spleber" acaba de llegar y debe ir al principio de la lista
#4.Cancelacion."Emma stone" aviso que no podra asistir
#5.seguridad.El ultimo  de la lista se porto mal y debe ser retirado.
#6.imprime la lista final y cuantos invitados queda en la lista 

#punto no.1
invitados = ["Robert Danny Jr","Emma Stone","Cillian Murphy"]
#punto no.2
invitados.append("Zendaya")
#punto no.3
invitados.insert(0,"Steven Sprelber")
#punto no.4
#invitados.pop(2)
invitados.remove("Emma stone")
#punto no.5
invitados.pop(3)
#punto no.6
print(invitados,"No total invitados: ",len(invitados))