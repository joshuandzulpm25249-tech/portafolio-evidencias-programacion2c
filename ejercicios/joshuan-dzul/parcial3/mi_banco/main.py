from banco import Banco
from cuenta import Cuenta

class Banco:
    def __init__(self):
        self.cuentas = []

    def registrar_cuenta(self,nueva_cuenta):
        self.cuentas.append(nueva_cuenta)
        print(f"¡cuenta creadacon exito para {nueva_cuenta.cliente}!")

    def transferir(self, origen, destino, cantidad):
        if origen.retirar(cantidad):
            destino.deposito(cantidad)
            return True
        return False

def main():
    mi_banco = Banco()
    
    while True:
        print("\n" + "="*35)
        print("   MENU DEL PROGRAMA MI BANCO   ")
        print("="*35)
        print("#1.- APERTURAR NUEVA CUENTA")
        print("#2.- VER CLIENTES")
        print("#3.- DEPOSITAR A CUENTA")
        print("#4.- RETIRAR DE UNA CUENTA")
        print("#5.- TRANSFERIR ENTRE CUENTAS")
        print("#6.- BUSCAR CUENTA")
        print("#7.- ELIMINAR UNA CUENTA")
        print("#8.- SALIR DEL PROGRAMA")
        print("="*35)
        
        opcion = input("Seleccione una opción (1-8): ").strip()
        
        if opcion == "1":
            print("\n--- APERTURAR NUEVA CUENTA ---")
            cliente = input("Nombre del titular de la cuenta: ").strip()
            num_cuenta = input("Número o identificador de la cuenta: ").strip()
            
            # Validación simple para el saldo inicial
            try:
                saldo_inicial = float(input("Saldo inicial (opcional, presiona Enter para 0): ") or 0)
            except ValueError:
                print("Saldo inválido. Se asignará 0 por defecto.")
                saldo_inicial = 0
            
            # Creamos el objeto de la clase Cuenta con los datos ingresados
            nueva_cuenta = Cuenta(cliente, num_cuenta, saldo_inicial)
            
            # Registramos la cuenta en la lista de nuestro banco
            mi_banco.registrar_cuenta(nueva_cuenta)
            
        elif opcion == "2":
            # Dejado como marcador para tu desarrollo futuro
            print("\nOpcion en desarrollo: VER CLIENTES")
            
        elif opcion == "3":
            print("\nOpcion en desarrollo: DEPOSITAR A CUENTA")
            
        elif opcion == "4":
            print("\nOpcion en desarrollo: RETIRAR DE UNA CUENTA")
            
        elif opcion == "5":
            print("\nOpcion en desarrollo: TRANSFERIR ENTRE CUENTAS")
            
        elif opcion == "6":
            print("\nOpcion en desarrollo: BUSCAR CUENTA")
            
        elif opcion == "7":
            print("\nOpcion en desarrollo: ELIMINAR UNA CUENTA")
            
        elif opcion == "8":
            print("\n¡Gracias por utilizar el programa Mi Banco! Saliendo...")
            break  # Rompe el ciclo while, terminando el programa de forma limpia
            
        else:
            # Si el usuario ingresa cualquier cosa que no sea del 1 al 8
            print("\n[ERROR] Opción no válida. Por favor, selecciona un número del 1 al 8.")

if __name__ == "__main__":
    main()