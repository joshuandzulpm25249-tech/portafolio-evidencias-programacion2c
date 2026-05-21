from cuenta import Cuenta

class Banco:

    def transferir(self, origen, destino, cantidad):
        if origen.retirar(cantidad):
            destino.depositar(cantidad)
            return True
        return False