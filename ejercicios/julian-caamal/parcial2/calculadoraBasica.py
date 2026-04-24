#funciones basicas
def suma (a,b):
    result = a + b
    return result

def resta (a,b):
    return a - b

def multi(a,b):
    return a * b

def div (a,b):
    return a / b
#menu de opciones
opcion = 0
while(opcion != 5):
    print("----menu de opciones ----")
    print("1. sumar 2 valores")
    print("2. restar 2 valores")
    print("3. multiplicar 2 valores")
    print("4. divicion 2 valores")
    print("5. terminar programa")
    opcion = int(input("\nSelecciona la opcion deseada [1-5]: "))
    
    if opcion == 1:
        #suma de dos numeros
        n1 = float(input("\ningresa el primer numero de sumar: "))
        n2 = float(input("ingresa el segundo valor de suma: "))
        print(f"resultado de la suma: {suma(n1,n2)}")
    elif opcion == 2:
        #resta de dos numeros
        n1 = float(input("\ningresa el minuendo: "))
        n2 = float(input("ingresa el sustraendo: "))
        print(f"diferencia de la resta: {resta(n1,n2)}")
    elif opcion == 3:
        #multiplicasion de dos numeros
        n1 = float(input("\ningresa el primer factor: "))
        n2 = float(input("ingresa el segundo factor: "))
        print(f"producto resultante: {multi(n1,n2)}")
    elif opcion == 4:
        #divicion de dos numeros
        n1 = float(input("\ningresa el dividendo: "))
        n2 = float(input("ingresa el divisor: "))
        print(f"cociente resultante: {div(n1,n2)}")
    elif opcion ==5:
        #finalizacion del programa
        print("programa finalisado...")
    else:
        print("opcion seleccionada no valida,inteta nueva mente")
