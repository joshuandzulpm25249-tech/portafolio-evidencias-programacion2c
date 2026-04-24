#Trabajas en la organización de un evento de premios.
# Tienes una lista de celebridades que entrarán por la alfombra roja.

# 1. Crea una lista llamada invitados con los nombres:
# "Robert Downey Jr.", "Emma Stone", "Cillian Murphy".
invitados = ["Robert Downey Jr.", "Emma Stone", "Cillian Murphy"]

# 2. Llega de último minuto. Agrega a "Zendaya" al final de la lista.
invitados.append("Zendaya")

# 3. Invitado VIP: "Steven Spielberg" debe ir al principio.
invitados.insert(0, "Steven Spielberg")

# 4. Cancelación: "Emma Stone" no asistirá.
invitados.remove("Emma Stone")

# 5. Imprime la lista final y cuántos quedan en total.
print("Lista final de invitados:", invitados)
print("Total de invitados:", len(invitados))