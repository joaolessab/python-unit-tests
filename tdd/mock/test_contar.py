import unittest
import contar

class TestContar(unittest.TestCase):

    def teste_deve_retornar_tamanho(self):
        # Act
        tamanho = contar.contar_arquivo()
        
        # Assert
        self.assertEqual(3, tamanho)