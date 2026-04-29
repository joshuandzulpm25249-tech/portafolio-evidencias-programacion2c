def formato_nombre(name, lastName):
    """
    Devuelve el nombre de usuario en el formato ""Apellido, Nombre".

    Argumentos:
      name(str): Primer nombre del usuario.
      lastName(str): Apellido paterno del usuario.

    Retorno:
    (str): El nombre completo en formato "Apellido, Nombre".
    """
    return f"{lastName}, {name}"

#funcion para la ejecucion del codigo
def main():
    __name = input("introduce el primer nombre: ")
    _lastName = input("introduce el primer apellido paterno: ")
    print(formato_nombre(__name,_lastName))
if __name__ == "__main__": 
    main()