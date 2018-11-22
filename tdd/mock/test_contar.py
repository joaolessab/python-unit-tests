import unittest
from unittest.mock import Mock, patch
import contar

class TestContar(unittest.TestCase):

    def teste_deve_contar_caracteres(self):
        tamanho = contar.contar_caracter("1234567890")

        self.assertEqual(10, tamanho)


    """def teste_deve_retornar_tamanho(self):
        # Act
        tamanho = contar.contar_arquivo()
        
        # Assert
        self.assertEqual(16, tamanho)

    @patch("builtins.open")
    def teste_deve_retornar_tamanho_mock(self, open_mock):
        # Arrange
        open_mock.return_value.read.return_value = "qualquer coisa"

        tamanho = contar.contar_arquivo()

        self.assertEqual(14, tamanho)"""