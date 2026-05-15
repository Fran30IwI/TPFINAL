class Juego:
    """Representa un videojuego dentro de la biblioteca."""

    def __init__(self, app_id: str, titulo: str, genero: str, desarrollador: str, anio: int, precio: float):
        self.__app_id = app_id
        self.__titulo = titulo
        self.__genero = genero
        self.__desarrollador = desarrollador
        self.__anio = anio
        self.__precio = precio

    # Getters
    def get_app_id(self) -> str:
        return self.__app_id

    def get_titulo(self) -> str:
        return self.__titulo

    def get_genero(self) -> str:
        return self.__genero

    def get_desarrollador(self) -> str:
        return self.__desarrollador

    def get_anio(self) -> int:
        return self.__anio

    def get_precio(self) -> float:
        return self.__precio

    def __str__(self):
        return (
            f"[{self.__app_id}] {self.__titulo} | "
            f"Género: {self.__genero} | "
            f"Dev: {self.__desarrollador} | "
            f"Año: {self.__anio} | "
            f"Precio: ${self.__precio:.2f}"
        )
