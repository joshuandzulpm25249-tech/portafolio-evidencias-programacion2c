#funciones basicas 
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def divicion(a,b):
    return a / b
    
#menu de opcionesdef suma(a,b):
opcion = 0
while(opcion != 5):
    print("---- \nmenu de opciones ----")
    print("1. sumar 2 valores")
    print("2. restar 2 valores")
    print("3. multiplicar 2 valores")
    print("4. dividir 2 valores")
    print("5. terminar programa")
    opcion = int(input("\nselecciona la opcion deseada [1-5]: "))

    if opcion == 1:
        #suma de 2 numeros
        n1 = float(input("\nIngresa el primer numero a sumar: "))
        n2 = float(input("\nIngresa el segundo numero a sumar: "))
        print(f"diferencia de la suma: {suma(n1,n2)}")
        
    elif opcion == 2:
        #resta de 2 numetos
        n1 = float(input("\nIngresa minuendo: "))
        n2 = float(input("\nIngresa el sustrayendo: "))
        print(f"cociente de la resta: {resta(n1,n2)}")
        
    elif opcion == 3:
        #multiplicacion de 2 numeros
        n1 = float(input("\nIngresa el primer factor: "))
        n2 = float(input("\nIngresa el segundo factor: "))
        print(f"producto resultante: {multiplicacion(n1,n2)}")
        
    elif opcion == 4:
        #divicion de 2 numeros
        n1 = float(input("\nIngresa el dividendo "))
        n2 = float(input("\nIngresa el divisor: "))
        print(f"cociente resultado: {divicion(n1,n2)}")
        
    elif opcion == 5:
        #finalizacion del programa
        print("programa finalizado...")

    else:
        #mensaje de error por opcion no valida
        print("opcion no valida,intenta nuevamente...")
        
