import unittest
from catalogo import Catalogo
from juego import Juego
from usuario import Usuario

class TestCajaNegra(unittest.TestCase):

    def setUp(self):
        self.catalogo = Catalogo()

    def test_usuario_duplicado(self):
        self.assertTrue(self.catalogo.registrar_usuario(Usuario("1","Juan")))
        self.assertFalse(self.catalogo.registrar_usuario(Usuario("1","Pedro")))

    def test_juego_duplicado(self):
        self.assertTrue(self.catalogo.agregar_juego(Juego("10","A","Accion","Dev",2024,10)))
        self.assertFalse(self.catalogo.agregar_juego(Juego("10","B","Accion","Dev",2024,10)))

    def test_usuario_inexistente(self):
        self.catalogo.agregar_juego(Juego("10","A","Accion","Dev",2024,10))
        self.assertFalse(self.catalogo.agregar_juego_a_usuario("999","10"))

    def test_juego_inexistente(self):
        self.catalogo.registrar_usuario(Usuario("1","Juan"))
        self.assertFalse(self.catalogo.agregar_juego_a_usuario("1","999"))

    def test_juego_repetido_en_biblioteca(self):
        self.catalogo.registrar_usuario(Usuario("1","Juan"))
        self.catalogo.agregar_juego(Juego("10","A","Accion","Dev",2024,10))
        self.assertTrue(self.catalogo.agregar_juego_a_usuario("1","10"))
        self.assertFalse(self.catalogo.agregar_juego_a_usuario("1","10"))

if __name__ == "__main__":
    unittest.main()
