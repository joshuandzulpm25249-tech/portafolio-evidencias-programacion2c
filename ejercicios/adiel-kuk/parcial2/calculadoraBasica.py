#funciones basicas
def suma(a,b):
    result = a + b

def resta(a,b):
    result = a - b

def multi(a,b):
    result = a * b

def division(a,b):
    return a / b
#menu de opciones
opcion = 0
while(opcion != 5):
    print("\n----Menu de opciones ----")
    print("1. Sumar 2 valores")
    print("2. Restar 2 valores")
    print("3. Multiplicar 2 valores")
    print("4. Dividir 2 valores")
    print("5. Terminar programa")
    opción =int(input("\nSelecciona la opción deseada [1-5]: "))

    if opcion == 1:
        #suma dos numeros
        n1 = float(input("\nIngresa el primer numero a sumar: "))
        n2 = float(input("Ingresa el segundo valor a sumar: "))
        print(f"Resultado de la suma: {suma(n1,n2)}")
    elif opción == 2:
        #Resta de dos numeros
        n1 = float(input("\nIngresa el minuendo: "))
        n2 = float(input("Ingresa el sustraendo: "))
        print(f"Diferencia de la resta: {resta(n1,n2)}")
    elif opción == 3:
        #multiplicacion de dos numeros
        n1 = float(input("\nIngresa el primer factor: "))
        n1 = float(input("\nIngresa el segundo factor: "))
        print(f"Producto resultante: {multi(n1,n2)}")
    elif opción == 4:
        #division de dos numeros
        n1 = float(input("\nIngresa el dividendo: "))
        n1 = float(input("\nIngresa el divisor: "))
        print(f"Cociente resultante: {division(n1,n2)}")
    elif opción == 5:
        #finalizacion del programa
        print("Programa finalizando...")
    else:
        print("opcion seleccionada no valida,intenta nueva mente")