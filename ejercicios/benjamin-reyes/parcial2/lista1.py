# listas1.py

"""
Trabajas en la organización de un evento de premios.
Tienes una lista de celebridades que entrarán por la alfombra roja. El orden es vital!
1. Crea una lista llamada invitados con los nombres: "Robert Downey Jr.", "Emma Stone" y "Cillian Murphy".
2. Llegada de último minuto. Agrega a "Zendaya" al final de la lista.
3. Invitado VIP: "Steven Spielberg" acaba de llegar y debe ir al principio de la lista.
4. Cancelación: "Emma Stone" avisa que no asistirá por seguridad. El último de la lista se porta mal y debe ser retirado.
5. Imprime la lista final y cuántos quedan en total.
"""

# Punto no. 1
invitados = ["Robert Downey Jr.", "Emma Stone", "Cillian Murphy"]
s
# Punto no. 2
invitados.append("Zendaya")

# Punto no. 3
invitados.insert(0, "Steven Spielberg")

# Punto no. 4
# "Emma Stone" avisa que no asistirá
invitados.remove("Emma Stone")

# El último de la lista se porta mal y debe ser retirado
invitados.pop()

# Punto no. 5
print("Lista final de invitados:", invitados)
print("Total de invitados:", len(invitados))
