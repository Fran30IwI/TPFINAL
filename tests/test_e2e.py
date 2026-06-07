import unittest
from catalogo import Catalogo
from juego import Juego
from usuario import Usuario

class TestE2E(unittest.TestCase):

    def test_flujo_completo_usuario_juego_biblioteca(self):
        catalogo = Catalogo()
        usuario = Usuario("1001", "Francisco")
        juego = Juego("2001", "Minecraft", "Sandbox", "Mojang", 2011, 29.99)

        self.assertTrue(catalogo.registrar_usuario(usuario))
        self.assertTrue(catalogo.agregar_juego(juego))
        self.assertTrue(catalogo.agregar_juego_a_usuario("1001", "2001"))

        usuario_recuperado = catalogo.buscar_usuario("1001")

        self.assertEqual(usuario_recuperado.total_juegos(), 1)
        self.assertTrue(usuario_recuperado.tiene_juego("2001"))
        self.assertAlmostEqual(usuario_recuperado.valor_biblioteca(), 29.99)

    def test_flujo_con_varios_juegos(self):
        catalogo = Catalogo()
        usuario = Usuario("1002", "Jugador")
        catalogo.registrar_usuario(usuario)

        catalogo.agregar_juego(Juego("1","Portal","Puzzle","Valve",2007,10))
        catalogo.agregar_juego(Juego("2","Half Life","FPS","Valve",2004,20))

        self.assertTrue(catalogo.agregar_juego_a_usuario("1002","1"))
        self.assertTrue(catalogo.agregar_juego_a_usuario("1002","2"))

        self.assertEqual(usuario.total_juegos(),2)
        self.assertEqual(usuario.valor_biblioteca(),30)

if __name__ == "__main__":
    unittest.main()
