import unittest
from unittest.mock import Mock, patch
import web_map_mais_acessados

class TestWebMapMaisAcessados(unittest.TestCase):
    
    def teste_lista_foi_preenchida(self):
        preencheu = web_map_mais_acessados.lista_foi_preenchida()
        
        self.assertTrue(preencheu)

    def teste_lista_e_valida(self):
        lista = web_map_mais_acessados.lista_e_valida()

        self.assertFalse(lista)

    def teste_lista_foi_filtrada(self):
        filtrada = web_map_mais_acessados.lista_foi_filtrada()

        self.assertTrue(5, filtrada)

    