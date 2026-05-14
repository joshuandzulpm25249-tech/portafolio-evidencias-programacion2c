import unittest
from cuenta import Cuenta

class TestCuenta(unittest.TestCase):

    def setUp(self):
        """
        Se ejecuta antes de cada prueba.
        """
        self.cuenta = Cuenta("Fulanito Perez Mengano", "001")

    #------------ Pruebas del Constructor ------------

    def test_validad_saldo(self):
        self.assertEqual(self.cuenta.saldo, 0, "El saldo inicial debe ser 0 por defecto")

    def test_valida_cliente(self):
        self.assertEqual(self.cuenta.Cliente, "Fulanito Perez Mengano", "El nombre del cliente no es correcto")

    #------------ Pruebas de Depósito ------------

    def test_depositar_dinero_valido(self):
        result = self.cuenta.deposito(500.00)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 500, "El saldo actual debería ser de 500.00")

    def test_depositar_dinero_negativa(self):
        result = self.cuenta.deposito(-200.00)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual debería ser de 0")

    #test para validar deposito en 0
    def test_depositar_dinero_cero(self):
        result = self.cuenta.deposito(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 0, "El saldo actual debería ser de 0")

    #------------ Pruebas de Retiro ------------
    def test_retirar_dinero_valido(self):
        self.cuenta.deposito(500.00)
        result = self.cuenta.retiro(200.00)
        self.assertTrue(result)
        self.assertEqual(self.cuenta.saldo, 300, "El saldo actual debería ser de 300.00")

    def test_retirar_dinero_mayor_saldo(self):
        self.cuenta.deposito(300.00)
        result = self.cuenta.retiro(400.00)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 300, "El saldo actual debería ser de 300.00")

    def test_retirar_dinero_negativa(self):
        self.cuenta.deposito(300.00)
        result = self.cuenta.retiro(-100.00)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 300, "El saldo actual debería ser de 300.00")

    #test para validar retiro en 0
    def test_retirar_dinero_cero(self):
        self.cuenta.deposito(300.00)
        result = self.cuenta.retiro(0)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 300, "El saldo actual debería ser de 300.00")
if __name__ == "__main__":
    unittest.main()

    #test para validar cantidad mayor la saldo
    def test_retirar_dinero_mayor_saldo(self):
        self.cuenta.deposito(300.00)
        result = self.cuenta.retiro(400.00)
        self.assertFalse(result)
        self.assertEqual(self.cuenta.saldo, 300, "El saldo actual debería ser de 300.00")

    