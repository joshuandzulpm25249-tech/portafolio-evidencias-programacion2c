from banco import Banco
from cuenta import Cuenta

def main():
    """MENU DEL PROGRAMA MI BANCO"""
    # Aquí puedes inicializar tu objeto Banco si lo necesitas
    # mi_banco = Banco() 
cuentas = {}

while True:
        print("\n" + "="*30)
        print("   MENU DEL PROGRAMA MI BANCO   ")
        print("="*30)
        print("1.- APERTURAR NUEVA CUENTA")
        print("2.- VER CLIENTES")
        print("3.- DEPOSITAR A CUENTA")
        print("4.- RETIRAR DE UNA CUENTA")
        print("5.- TRANSFERIR ENTRE CUENTAS")
        print("6.- BUSCAR CUENTA")
        print("7.- ELIMINAR UNA CUENTA")
        print("8.- SALIR DEL PROGRAMA")
        print("="*30)
        
        opcion = input("Selecciona una opción (1-8): ")
        
        #apertura de la cuenta
        if opcion == "1":
            print("\n--- Aperturando nueva cuenta ---")
            nombre = input("Ingrese el nombre del cliente: ")
            cuenta = input("Ingrese el número de cuenta: ")
            saldo_inicial = float(input("Ingrese el saldo inicial: "))
            cuentas[cuenta] = [nombre, saldo_inicial]       
        
        #ver clientes registrados
        elif opcion == "2":
            print("\n--- Clientes Registrados ---")
            if not cuentas:
                print("No hay clientes registrados.")
            else: 
                for cuenta, datos in cuentas.items():
                    print(f"Cuenta: {cuenta}, Nombre: {datos[0]}, Saldo: {datos[1]}")

        #depositar a cuenta
        elif opcion == "3":
            cuenta = input("Ingrese el número de cuenta para depositar: ")
            if cuenta in cuentas:
                nombre = ("Ingrese el nombre del cliente: ")
                dinero = float(input("Ingrese la cantidad a depositar: "))
                cuentas[cuenta][1] += dinero
                print(f"Depósito exitoso. Nuevo saldo: {cuentas[cuenta][1]}")
            else:
                print("Cuenta no encontrada.")

        #retirar de una cuenta   
        elif opcion == "4":
            cuenta = input("Ingrese el número de cuenta para retirar: ")
            if cuenta in cuentas:
                dinero = float(input("Ingrese la cantidad a retirar: "))
                if cuentas[cuenta][1] >= dinero:
                    cuentas[cuenta][1] -= dinero
                    print(f"Retiro exitoso. Nuevo saldo: {cuentas[cuenta][1]}")
                else:
                    print("Saldo insuficiente.")
            else:
                print("Cuenta no encontrada.")

        #transferir entre cuentas    
        elif opcion == "5":
            cuenta_origen = input("Ingrese el número de cuenta de origen: ")
            cuenta_destino = input("Ingrese el número de cuenta de destino: ")
            if cuenta_origen in cuentas and cuenta_destino in cuentas:
                dinero = float(input("Ingrese la cantidad a transferir: "))
                if cuentas[cuenta_origen][1] >= dinero:
                    cuentas[cuenta_origen][1] -= dinero
                    cuentas[cuenta_destino][1] += dinero
                    print(f"Transferencia exitosa. Nuevo saldo en cuenta origen: {cuentas[cuenta_origen][1]}, Nuevo saldo en cuenta destino: {cuentas[cuenta_destino][1]}")
                else:
                    print("Saldo insuficiente en la cuenta de origen.")
            else:
                print("Una o ambas cuentas no fueron encontradas.")

        #buscar cuenta    
        elif opcion == "6":
            cuenta = input("Ingrese el número de cuenta para buscar: ")
            if cuenta in cuentas:
                print(f"Cuenta: {cuenta}, Nombre: {cuentas[cuenta][0]}, Saldo: {cuentas[cuenta][1]}")
            else:
                print("Cuenta no encontrada.")

        #eliminar cuenta    
        elif opcion == "7":
            cuenta = input("Ingrese el número de cuenta para eliminar: ")
            if cuenta in cuentas:
                del cuentas[cuenta]
                print("Cuenta eliminada exitosamente.")
            else:
                print("Cuenta no encontrada.")

        elif opcion == "8":
            print("¡Gracias por usar el sistema de Mi Banco! Hasta luego.")
            break 
            
        else:
            print("Opción no válida. Por favor, elige un número del 1 al 8.")

if __name__ == "__main__":
    main()

