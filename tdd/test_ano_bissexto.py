import unittest
import ano_bissexto

class TestAnoBissexto(unittest.TestCase):

    # Não é necessário fazer assert pois o Thrown já irá retornar erro
    def teste_roda(self):
        ano_bissexto.e_bissexto(1)

    def teste_regra_divisivel_400(self):
        valor400 = ano_bissexto.e_bissexto(400)
        valor800 = ano_bissexto.e_bissexto(800)
        
        self.assertTrue(valor400)
        self.assertTrue(valor800)

    def teste_regra_divisivel_400_negativo(self):
        valor = ano_bissexto.e_bissexto(401)
        self.assertFalse(valor)

    def teste_regra_divisivel_100(self):
        valor = ano_bissexto.e_bissexto(300)
        self.assertFalse(valor)

    def teste_regra_divisivel_4(self):
        valor = ano_bissexto.e_bissexto(16)
        self.assertTrue(valor)