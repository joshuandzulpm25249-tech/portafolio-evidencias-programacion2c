def formato_nombre(name, lastname):
    """
    Devuelve el nombre de usuario en el formato Apellido, Nombre.

    Argumentos:
        name (atr): Primer nombre del usuario.
        lastName (str): Apellido paterno del usuario.

    Retorno:
        (str): El nombre completo en formato Apellido, Nombre.
    """
    return f"{lastname}, {name}"

#Funcion name para ejecución del código.
def main():
    _name = input("Introduce tu primer nombre: ")
    _lastName = input("Introduce tu apellido paterno: ")
    print(formato_nombre(_name,_lastName))

    if __name__=="_name_":
        main()

