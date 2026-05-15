from juego import Juego
from usuario import Usuario


class Catalogo:
    """Gestiona el catálogo global de juegos y los usuarios registrados."""

    def __init__(self):
        self.__juegos: list[Juego] = []
        self.__usuarios: list[Usuario] = []

    # ── Alta ─────────────────────────────────────────────────────────────────

    def agregar_juego(self, juego: Juego) -> bool:
        """Agrega un juego al catálogo. Retorna False si el ID ya existe."""
        if self.buscar_juego_por_id(juego.get_app_id()):
            print(f" Ya existe un juego con App ID '{juego.get_app_id()}'.")
            return False
        self.__juegos.append(juego)
        print(f"'{juego.get_titulo()}' agregado al catálogo.")
        return True

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un usuario. Retorna False si el Steam ID ya existe."""
        if self.buscar_usuario(usuario.get_steam_id()):
            print(f" Ya existe un usuario con Steam ID '{usuario.get_steam_id()}'.")
            return False
        self.__usuarios.append(usuario)
        print(f"Usuario '{usuario.get_nombre()}' registrado.")
        return True

    # ── Búsqueda ─────────────────────────────────────────────────────────────

    def buscar_juego_por_id(self, app_id: str) -> Juego | None:
        for juego in self.__juegos:
            if juego.get_app_id() == app_id:
                return juego
        return None

    def buscar_juegos_por_titulo(self, titulo: str) -> list[Juego]:
        """Búsqueda parcial por título (sin distinguir mayúsculas)."""
        termino = titulo.lower()
        return [j for j in self.__juegos if termino in j.get_titulo().lower()]

    def buscar_juegos_por_genero(self, genero: str) -> list[Juego]:
        """Filtra todos los juegos de un género."""
        termino = genero.lower()
        return [j for j in self.__juegos if termino in j.get_genero().lower()]

    def buscar_usuario(self, steam_id: str) -> Usuario | None:
        for usuario in self.__usuarios:
            if usuario.get_steam_id() == steam_id:
                return usuario
        return None

    # ── Agregar juego a biblioteca de usuario ─────────────────────────────────

    def agregar_juego_a_usuario(self, steam_id: str, app_id: str) -> bool:
        """Añade un juego del catálogo a la biblioteca personal de un usuario."""
        usuario = self.buscar_usuario(steam_id)
        juego = self.buscar_juego_por_id(app_id)

        if not usuario:
            print(" Usuario no encontrado.")
            return False
        if not juego:
            print(" Juego no encontrado en el catálogo.")
            return False
        if usuario.tiene_juego(app_id):
            print(f" '{usuario.get_nombre()}' ya tiene '{juego.get_titulo()}' en su biblioteca.")
            return False

        usuario.agregar_juego(juego)
        print(f" '{juego.get_titulo()}' agregado a la biblioteca de {usuario.get_nombre()}.")
        return True

    # ── Listados ─────────────────────────────────────────────────────────────

    def listar_catalogo(self):
        if not self.__juegos:
            print("No hay juegos en el catálogo.")
            return
        print(f"\n{'─'*60}")
        print(f"  CATÁLOGO GLOBAL — {len(self.__juegos)} juego(s)")
        print(f"{'─'*60}")
        for juego in self.__juegos:
            print(juego)

    def listar_usuarios(self):
        if not self.__usuarios:
            print("No hay usuarios registrados.")
            return
        print(f"\n{'─'*60}")
        print(f"  USUARIOS REGISTRADOS — {len(self.__usuarios)} usuario(s)")
        print(f"{'─'*60}")
        for usuario in self.__usuarios:
            print(usuario)

    def listar_biblioteca_usuario(self, steam_id: str):
        usuario = self.buscar_usuario(steam_id)
        if not usuario:
            print(" Usuario no encontrado.")
            return
        biblioteca = usuario.get_biblioteca()
        print(f"\n{'─'*60}")
        print(f"  Biblioteca de {usuario.get_nombre()} — {len(biblioteca)} juego(s)")
        print(f"{'─'*60}")
        if not biblioteca:
            print("  (sin juegos)")
        for juego in biblioteca:
            print(juego)
