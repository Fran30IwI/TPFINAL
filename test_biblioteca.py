import unittest
import logging

from juego import Juego
from usuario import Usuario
from catalogo import Catalogo


# CONFIGURACION DEL LOG
logging.basicConfig(
    filename="test_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    force=True
)


class TestJuego(unittest.TestCase):

    def test_constructor(self):

        juego = Juego("730", "CS2", "FPS", "Valve", 2023, 0.00)

        self.assertEqual(juego.get_app_id(), "730")

        logging.info("TestJuego.test_constructor OK")


class TestUsuario(unittest.TestCase):

    def test_agregar_juego(self):

        usuario = Usuario("001", "Juan")

        juego = Juego("730", "CS2", "FPS", "Valve", 2023, 0.00)

        usuario.agregar_juego(juego)

        self.assertEqual(usuario.total_juegos(), 1)

        logging.info("TestUsuario.test_agregar_juego OK")


class TestIntegracion(unittest.TestCase):

    def test_agregar_juego_usuario(self):

        catalogo = Catalogo()

        usuario = Usuario("001", "Juan")

        catalogo.registrar_usuario(usuario)

        juego = Juego("730", "CS2", "FPS", "Valve", 2023, 0.00)

        catalogo.agregar_juego(juego)

        resultado = catalogo.agregar_juego_a_usuario("001", "730")

        self.assertTrue(resultado)

        logging.info("TestIntegracion.test_agregar_juego_usuario OK")


if __name__ == "__main__":

    logging.info("INICIO DE TEST")

    unittest.main()

    logging.info("FIN DE TEST")