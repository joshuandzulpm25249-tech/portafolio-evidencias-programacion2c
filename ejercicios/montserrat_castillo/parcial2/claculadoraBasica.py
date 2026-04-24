#Funciones basicas
def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multi(a,b):
    return a * b

def div(a,b):
    return a / b

#menu de opciones
opcion = 0
while(opcion != 5):
    print("---- Menu de opciones ----")
    print("1. Sumar 2 valores")
    print("2. Restar 2 valores")
    print("3. Multiplica 2 valores")
    print("4. Dividir 2 valores")
    print("5. Terminar programa")
    opcion = int(input("\nSelesciona la opcion desea [1-5]: "))

    if opcion == 1 :
        #suma de dos numeros
        n1 = float(input("\nIngresa el primer numero a sumar: "))
        n2 = float(input("Ingrsa el segundo valor a sumar: "))
        print(f"Resultados de la suma: {suma}")
    elif opcion == 2 :
        #resta de dos numeros
        n1 = float(input("\nIngresa el minuendo: "))
        n2 = float(input("Ingrsa el sustraendo: "))
        print(f"cociente de la resta: {resta(n1,n2)}")
    elif opcion == 3 :
        #multiplicacion de dos numeros
        n1 = float(input("\nIngresa el primer factor: "))
        n2 = float(input("Ingrsa el segundo valor: "))
        print(f"producto resultante: {multi(n1,n2)}")
    elif opcion == 4 :
        #division de dos numeros
        n1 = float(input("\nIngresa el dividiendo: "))
        n2 = float(input("Ingrsa el divisor: "))
        print(f"cociente resultado: {div(n1,n2)}")
    elif opcion == 5 :
        #finalizacicon del programa
        print("Programa finalizado...") 
    else:
        #mensaje de error por opcion no valida
        print("Opcion seleccionada no valida, intenta nuvamente!")
