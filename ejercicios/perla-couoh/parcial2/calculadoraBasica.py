#funciones Basicas 
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a,b):
    return a * b

def division(a,b):
    return a / b

#menu de opciones
opcion = 0
while(opcion != 5):
    print("----Menu de opciones")
    print("1. Sumar 2 valores")
    print("2. Restar 2 valores")
    print("3. Multiplicar 2 valores")
    print("4. Dividir 2 valores")
    print("5. Terminar programa")
    opcion = int(input("\nSelecciona la opcion deseada [1-5]: "))
    
    if opcion == 1:
        #Suma de dos numeros
        n1 = float(input("\Ingresa el primer numero a sumar: "))
        n2 = float(input("\Ingresa el segundo nuemro a restar: "))
        print(f"Resultado de la suma: {suma(n1,n2)}")
    elif opcion == 2:
        #Resta de dos numeros
        n1 = float(input("\Ingresa el minuendo: "))
        n2 = float(input("\Ingresa el sustraendo: "))
        print(f"Diferencia de la resta: {resta(n1,n2)}")
    elif opcion == 3:
        #Multiplicacion de dos numeros
        n1 = float(input("\Ingresa el primer factor: "))
        n1 = float(input("\Ingresa el segundo factor: "))
        print(f"Producto resultante: {multi(n1,n2)}")
    elif opcion == 4:
        #Division de dos numeros
        n1 = float(input("\Ingresa el dividendo: "))
        n1 = float(input("\Ingresa el divisor: "))
        print(f"Cociente resultante: {multi(n1,n2)}")
    elif opcion == 5:
        #Finalizacion del programa
        print("Programa finalizado...")
    else:
        #Mensaje de error por opcion no valida
        print("¡Opcion no valida, intenta nuevamente!")