#funciones basicas 
def suma(a,b):
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division (a,b):
    return a/b

def multiplicacion(a,b):
    return a,b

#menu de opciones
opcion=0
while(opcion !=5):
    print( "---menu de opciones---")
    print ("1. sumar 2 valores")
    print("2. restar 2 valores")
    print("3. multiplicar 2 valores")
    print("4. dividir 2 valores")
    print("5. terminar programa")
    print(("\nseleciona la opcion deseada[1-5]"))
    opcion = int(input("\nseleciona la opcion deseada[1-5]"))
    if opcion ==1:
        #suma de dos numeros
        n1=float(input("\nIngresa el primer numero a sumar"))
        n2=float(input("\ningresa el segundo numero a sumar"))
        print(f"resultado de la suma{suma(n1,n2)}")

    elif opcion == 2:
        #resta de 2 numeros 
        n1=float(input("\nIngresa el minuendo"))
        n2=float(input("\ningresa el sustrayendo"))
        print(f"cociente de la resta{resta(n1,n2)}")

    elif opcion == 3:
        #multiplicacion de 2 numeros
        n1=float(input("\nIngresa el primer factor"))
        n2=float(input("\ningresa el segundo factor"))
        print(f"producto resultante {multiplicacion(n1,n2)}")

    elif opcion == 4:
        #division de 3 numeros
        n1=float(input("\nIngresa el dividendo"))
        n2=float(input("\ningresa el divisor"))
        print(f"cociente resultante{division(n1,n2)}")

    elif opcion == 5:
        #finalizacion del rograma 
        print("programa finalizado...")

    else:
        #"mensaje de error por mensaje no valido"
        print("opcion seleccionada no valida, intenta de nuevo")