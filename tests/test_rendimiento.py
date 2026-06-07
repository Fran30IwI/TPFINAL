import unittest
import time
from catalogo import Catalogo
from juego import Juego

class TestRendimiento(unittest.TestCase):

    def test_busqueda_catalogo_grande(self):
        catalogo = Catalogo()

        for i in range(5000):
            catalogo.agregar_juego(Juego(str(i), f"Juego {i}", "Accion", "Dev", 2024, 10))

        inicio = time.perf_counter()
        resultado = catalogo.buscar_juegos_por_titulo("Juego 4999")
        fin = time.perf_counter()

        self.assertEqual(len(resultado), 1)
        self.assertLess(fin - inicio, 1)

if __name__ == "__main__":
    unittest.main()
