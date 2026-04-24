#funcioness basicas 
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a,b):
    return a * b

def division (a,b):
    return a / b
#menu de opciones
opcion = 0
while(opcion != 5):
    print("---- Menu de opciones ----")
    print("1. sumar 2 valores")
    print("2. restar 2 valores")
    print("3. Multiplicar 2 valores")
    print("4. dividir 2 valores")
    print("5. Terminar el programa")
    print("\nselecciona la opcion deseada [1-5]: ")
    opcion = int(input("\nselecciona la opcion deseada [1-5]: "))

    if opcion == 1:
        #suma de dos numeros
        n1 = float(input("\nIngresa el primer numero a sumar: "))
        n2 = float(input("Ingresa el segundo valor a sumar: "))
        print(f"Resultado de la suma: {suma(n1,n2)}")
    elif opcion == 2:
        #Resta de dos numeros
        n1 = float(input("\nIngresa el primer numero a minuendo: "))
        n2 = float(input("Ingresa el segundo valor a sustraendo: "))
        print(f"Diferencia de la resta {(n1,n2)}")
    elif opcion == 3:
        #Multiplicacion de dos numeros
        n1 = float(input("\nIngresa el primer numero a primer factor: "))
        n2 = float(input("Ingresa el segundo valor a segundo factor: "))
        print(f"producto resultante: {multi(n1,n2)}")
    elif opcion == 4:
        #Division de dos numeros
        n1 = float(input("\nIngresa el primer numero a dividendo: "))
        n2 = float(input("Ingresa el segundo valor a divisor: "))
        print(f"Cociente resultante: {division(n1,n2)}")
    elif opcion == 5:
        #Finalixar el programa
        print("programa finalizado...")
    else:
        #mensaje de error por opcion no valida
        print("opcion seleccionada no valida, intenta nuevamente")