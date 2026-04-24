#Funciones bascicas
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a,b):
    return a * b

def div(a,b):
    return a / b
#Menu de opciones

opcion = 0
while(opcion != 5):
    print("----Menu de opciones----")
    print("1. Sumar 2 valores")
    print("2. Restar 2 valores")
    print("3. Multiplicar 2 valores")
    print("4. Dividir 2 valores")
    print("5. Terminar programa")
    opcion = int(input("\nSeleciona la opcion deseada [1-5]: "))

    if opcion == 1:
        #Suma de dos valores
        v1 = float(input("\nIngresa el primer valor a sumar: "))
        v2 = float(input("Ingresa el segundo valor a sumar: "))
        print(f"El resultado de la suma: {suma(v1,v2)}")
    elif opcion == 2:
        #Resta de dos valores
        v1 = float(input("\nIngresa el minuendo: "))
        v2 = float(input("Ingresa el sustrando: "))
        print(f"Cociente de la resta: {resta(v1,v2)}")
    elif opcion == 3:
        #Multiplicacion de dos valores
        v1 = float(input("\nIngresa el primer multiplo: "))
        v2 = float(input("Ingresa el segundo multiplo: "))
        print(f"Producto resultante: {multi(v1,v2)}")
    elif opcion == 4:
        #Division de dos valores
        v1 = float(input("\nIngresa el dividendo: "))
        v2 = float(input("Ingresa el divisor: "))
        print(f"Cociente resultante; {div(v1,v2)}")
    elif opcion == 5:
        #Finalizando el programa 
        print("Programa finalizado...")
    else:
        #Mensaje de error por opcion invalida 
        print("¡Opcion no valida, intenta nuevamente!")    
