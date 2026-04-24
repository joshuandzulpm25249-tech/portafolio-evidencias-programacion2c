#funciones basicas 
def suma(a,b):
    return a + b

def resta(a,b):
    return a-b

def multiplicar(a,b):
    return a*b

def division(a,b):
    return a/b

#menu de opciones
opcion = 0
while(opcion != 5):
    print("---- Menu de opciones ----")
    print("1 sumar 2 valores")
    print("2 restar 2 valores")
    print("3 multiplicar 2 valores")
    print("4 dividir 2 valores")
    print("5 terminar programa")
    opcion = int(input("\nSelecciona la opccion deseada [1-5]: "))

    if opcion == 1:
#suma de dos numeros 
     n1 = float(input("\n ingresa el primer numero a sumar: "))
     n2 = float(input("\n ingresa el segundo valor a sumar: "))
     print(f"resultado de la suma: {suma}")
    elif opcion == 2:
     n1 = float(input("\n ingresa el primer numero a restar: "))
     n2 = float(input("\n ingresa el segundo numero a restar: "))
     print(f"resultado de la resta: {resta(n1,n2)}")
    elif opcion == 3:
     n1 = float(input("\n ingresa el primer numer a multiplicar: "))
     n2 = float(input("\n ingresa el segundo numero a multiplicar: "))
     print(f"producto resultante: {multiplicar(n1,n2)}")
    elif opcion == 4:
     n1 =float(input("\n ingresa el primer numero a dividir: "))
     n2 = float(input("\n ingresa el segundo numero a dividir: "))
     print(f"cocient resultado: ")
    elif opcion == 5:
        print("Programa finalizado...")
    else:
       print("opcion seleccionada noo valida intenta de nuevo!")
