#Funciones basicas 
def suma (a,b):
    result = a + b
    return result

def resta (a,b):
    result = a - b
    return result

def multiplicacion (a,b):
    result = a * b
    return result
def division (a,b):
    result = a / b
    return result

opcion = 0
#Menu de opciones
while(opcion !=5):
    print("--- Menu de opciones---")
    print("1. Sumar 2 valores")
    print("2. Restar 2 valores")
    print("3. Multiplicar 2 valores")
    print("4. Dividir 2 valores")
    print("5. Terminar programa")
    opcion = int(input("\nSelecciona la opcion deseada [1-5]: "))
    if opcion == 1:
        #Suma de 2 numeros
        n1 = float(input("\nIngresa el primer valor a sumar:"))
        n2 = float(input("Ingresa el segundo valor a sumar: "))
        print(f"Resultado de la suma: {suma(n1,n2)}")
    elif opcion == 2:
        #Resta de 2 numeros
        n1 = float(input("\nIngresa el minuendo: "))
        n2 = float(input("Ingresa el sustraendo: "))
        print(f"diferencia de la resta: {resta(n1,n2)}")
    elif opcion == 3:
        #multiplicacion de 2 numeros
        n1 = float(input("\nIngresa el primer factor:"))
        n2 = float(input("Ingresa el segundo favtor: "))
        print(f"Producto resultante: {multiplicacion(n1,n2)} ")
    elif opcion == 4:
        #Division de 2 numeros
         n1 = float(input("\nIngresa el dividendo: "))
         n2 = float(input("Ingresa el  divisor: "))
         print(f"Cociente resultante: {division(n1,n2)}")
    elif opcion == 5:
        #Finalizacion del programa
        print("Programa finalizado...")
    else:
        #Mensaje de error por opcion no valida
        print("Opcion seleccionada no valida, intentalo nuevamente")