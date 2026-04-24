def formato_nombre(name, lastName):
    """
    Devuelve el nombre de usuario en el formato apellido, nombre

    Argumentos:
    name (str): Primer nombre del usuario.
    lastname (stsr): Apellido paterno del usuario.

Retorno:
    (str): El nombre completo en formato apellido, nombre
"""
    return f"{lastName}, {name}"

#funcion main para la ejecucion del codigo.

def main():
   _name= input ("Introduce tu primer nombre")
   _lastName= input ("Inttroduce tu apellido paterno")
   print(formato_nombre(_name,_lastName))

if __name__=="__main__":
    main()