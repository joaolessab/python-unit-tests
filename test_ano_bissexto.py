import unittest
import ano_bissexto

class TestAnoBissexto(unittest.TestCase):
    
    def test_para_2000(self):
        valor = ano_bissexto.e_bissexto(2000)
        self.assertTrue(valor)

    def test_para_2005(self):
        valor = ano_bissexto.e_bissexto(2005)
        self.assertFalse(valor)

    def test_para_2004(self):
        valor = ano_bissexto.e_bissexto(2004)
        self.assertFalse(valor)

    def test_para_none(self):
        self.assertRaises(ValueError, ano_bissexto.e_bissexto, None)