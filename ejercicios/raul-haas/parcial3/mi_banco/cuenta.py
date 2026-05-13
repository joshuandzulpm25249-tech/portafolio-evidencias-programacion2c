class Cuenta:

    def __init__(self, cliente, cuenta, saldo):
        """
        Inicializa una nueva instancia de la clase Cuenta.

        Args:
            cliente (str): El nombre del dueño de la cuenta.
            cuenta (str): El número de cuenta.
            saldo (float): El saldo inicial de la cuenta.
        """
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo
    
    def deposito(self, cantidad):
        """
        Suma una cantidad de dinero al saldo actual si la cantidad es positiva.

        Args:
            cantidad (float): Monto a depositar.

        Returns:
            bool: True si el depósito fue exitoso, False en caso contrario.
        """
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False
    
    def retirar(self, cantidad):
        """
        Resta una cantidad de dinero al saldo actual si hay fondos suficientes.

        Args:
            cantidad (float): Monto a retirar.

        Returns:
            bool: True si el retiro se pudo realizar, False si no hay saldo o es inválido.
        """
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False
    
def main():
    
    # Creación de objeto
    mi_cuenta = Cuenta("Ana Pérez", "123456-78", 1000.0)
    
    print(f"Bienvenido/a {mi_cuenta.cliente}")
    print(f"Saldo actual: ${mi_cuenta.saldo}")

if __name__ == "__main__":
    # El bloque if __name__ == "__main__": asegura que main() solo se ejecute 
    # si el archivo se lanza directamente, y no si se importa como módulo.
    main()