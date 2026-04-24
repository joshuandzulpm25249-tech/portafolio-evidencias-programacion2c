def formato_nombre(name, lastName):
    """
    Devuelve el nombre de usuario en el formato  Apllido,Nombre.

    Argumentos:
    name(str):primer nombre del usuario
    lastName (str): Aperllido paterno del uasuario.

    Retorn:
        (str): El nombre completo en formato Apellido,Nombre.
    """
    return f"{lastName},{name}"

#Funcion main para ejecucion de codigo.

def main():
    _name = input("Introduce tu primer nombre: ")
    _lastName = input("Introduce tu apellido paterno: ")
    print(formato_nombre(_name,_lastName))

if __name__== "_main_":
   main()