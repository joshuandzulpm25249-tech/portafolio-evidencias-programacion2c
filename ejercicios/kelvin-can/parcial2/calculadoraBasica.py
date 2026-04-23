#funciones basicas
def suma(a,b):
    result = a + b
    return result


def resta(a,b):
    result = a - b
    return result

def multi(a,b):
    result = a * b
    return result

def division (a,b):
    result = a / b
    return result
#menu de opciones
opcion = 0
while(opcion != 5):
    print("---Menu de opciones---")
    print("1. Sumar 2 valores")
    print("2. Restar 2 valores")
    print("3. Multiplicar 2 valores") 
    print("4. Dividir 2 valores")
    print("5. Terminar programa")
    opcion = int(input("\nSelecciona la opcion deseada[1-5]: "))

if opcion == 1:
        #Suma de dos numeros
        n1 = float(input("\nIngresa el primer numero a sumar: "))
        n2 = float(input("\nIngresa el segundo numero a sumar: "))
        print(f"Diferencia de la suma: {suma(n1,n2)}")

elif opcion == 2:
        #Resta de dos numeros
        n1 = float(input("\nIngresa el minuendo: "))
        n2 = float(input("\nIngresa el sustraendo: "))
        print(f"Diferencia de la resta: {resta(n1.n2)}")

elif opcion == 3:
        #Multiplicacionde dos numeros
        n1 = float(input("\nIngresa el primer factor: "))
        n2 = float(input("\nIngresa el segundo factor: "))
        print(f"Producto resultante {multi(n1,n2)}")

elif opcion == 4:
        #Division de dos numeros
        n1 = float(input("\nIngresa el dividiendo: "))
        n2 = float(input("\nIngresa el divisor: "))
        print(f"Cociente resultante: {division(n1,n2)}")

elif opcion == 5:
        #Finalizacion del programa
        print("programa finalizado...")
else:
        #Mensaje de error por opcion no valida
        print("Opcion seleccionada no valida,intenta de nuevo")