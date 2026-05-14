import unittest
from parcial3.mi_calculadora.src.operaciones import suma, resta, multiplicacion, division

class TestOperaciones(unittest.TestCase):
    
    def Test_suma_positivos(self):
        self.assertEqual(suma(300,3), 303)
        
    def Test_suma_negativos(self):
        self.assertEqual(suma(-4,-6), -10)
    
    def Test_resta_basica(self):
        self.assertEqual(resta(10,5),5 )
        
    def Test_resta_negativa(self):
        self.assertEqual(resta(10,30), -20)
    
    def Test_resta_valoresNegativos(self):
        self.assertEqual(resta(-5,-5), 0)
        
if __name__ == '__main__':
    unittest.main()