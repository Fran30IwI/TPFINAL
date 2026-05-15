from juego import Juego


class Usuario:
    """Representa un usuario con su biblioteca personal de juegos."""

    def __init__(self, steam_id: str, nombre: str):
        self.__steam_id = steam_id
        self.__nombre = nombre
        self.__biblioteca: list[Juego] = []

    # Getters
    def get_steam_id(self) -> str:
        return self.__steam_id

    def get_nombre(self) -> str:
        return self.__nombre

    def get_biblioteca(self) -> list[Juego]:
        return self.__biblioteca

    def tiene_juego(self, app_id: str) -> bool:
        """Verifica si el usuario ya posee un juego."""
        return any(j.get_app_id() == app_id for j in self.__biblioteca)

    def agregar_juego(self, juego: Juego):
        self.__biblioteca.append(juego)

    def total_juegos(self) -> int:
        return len(self.__biblioteca)

    def valor_biblioteca(self) -> float:
        """Calcula el valor total de la biblioteca del usuario."""
        return sum(j.get_precio() for j in self.__biblioteca)

    def __str__(self):
        return (
            f"Usuario: {self.__nombre} (ID: {self.__steam_id}) | "
            f"Juegos: {self.total_juegos()} | "
            f"Valor biblioteca: ${self.valor_biblioteca():.2f}"
        )
