import unittest
from mi_calculadora.src.operaciones import suma,resta,multiplicacion,division,potencia

class TestOperaciones(unittest.TestCase):

    def Test_suma_(self):
        self.assertEqual(suma(2, 4), 6)


    def Test_resta_(self):
        self.assertEqual(resta(10, 4), 6)


    def Test_multiplicacion(self):
        self.assertEqual(multiplicacion(10, 3), 30)
    
    def Test_division(self):
        self.assertEqual(division(10, 2), 5)

    def Test_potencia(self):
        self.assertEqual(potencia(2, 2), 4)

if __name__ == '__main__':
    unittest.main()              