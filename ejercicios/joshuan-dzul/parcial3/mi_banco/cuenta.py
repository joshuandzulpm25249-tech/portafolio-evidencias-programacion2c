class Cuenta:

    def __init__(self, cliente, cuenta, saldo=0):
        """
        Constructor de la clase Cuenta.

        Args:
            cliente (str): Nombre del titular de la cuenta.
            cuenta (str): Número o identificador de la cuenta.
            saldo (float, opcional): Saldo inicial de la cuenta. Por defecto es 0.
        """
        self.cliente = cliente
        self.cuenta = cuenta
        self.saldo = saldo

    def deposito(self, cantidad):
        """
        Realiza un depósito en la cuenta.

        Args:
            cantidad (float): La cantidad a depositar. Debe ser un valor positivo.

        Returns:
            bool: True si el depósito fue exitoso, False si la cantidad es inválida.
        """
        if cantidad > 0:
            self.saldo += cantidad
            return True
        return False

    def retirar(self, cantidad):
        """
        Realiza un retiro de la cuenta.

        Args:
            cantidad (float): La cantidad a retirar. Debe ser un valor positivo y no puede exceder el saldo disponible.

        Returns:
            bool: True si el retiro fue exitoso, False si la cantidad es inválida o insuficiente.
        """
        if cantidad > 0 and cantidad <= self.saldo:
            self.saldo -= cantidad
            return True
        return False

if __name__ == "__main__":
    main()
