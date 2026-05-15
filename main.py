from catalogo import Catalogo
from juego import Juego
from usuario import Usuario


def cargar_datos_prueba(catalogo: Catalogo):
    """Precarga juegos y usuarios de ejemplo para facilitar las pruebas."""
    juegos = [
        Juego("730",   "Counter-Strike 2",        "FPS",       "Valve",            2023, 0.00),
        Juego("570",   "Dota 2",                  "MOBA",      "Valve",            2013, 0.00),
        Juego("1086940", "BATTLEGROUNDS (PUBG)",   "Battle Royale", "Krafton",      2017, 29.99),
        Juego("1245620", "Elden Ring",             "RPG",       "FromSoftware",     2022, 59.99),
        Juego("1172470", "Apex Legends",           "Battle Royale", "Respawn",      2020, 0.00),
        Juego("271590", "GTA V",                   "Acción",    "Rockstar Games",   2015, 29.99),
        Juego("2050650", "Hogwarts Legacy",        "RPG",       "Avalanche Software",2023, 59.99),
        Juego("1091500", "Cyberpunk 2077",         "RPG",       "CD Projekt Red",   2020, 39.99),
    ]
    for j in juegos:
        catalogo.agregar_juego(j)

    usuarios = [
        Usuario("76561001", "GamerX"),
        Usuario("76561002", "ProPlayer99"),
    ]
    for u in usuarios:
        catalogo.registrar_usuario(u)

    # Algunos juegos precargados en las bibliotecas
    catalogo.agregar_juego_a_usuario("76561001", "730")
    catalogo.agregar_juego_a_usuario("76561001", "1245620")
    catalogo.agregar_juego_a_usuario("76561002", "570")
    catalogo.agregar_juego_a_usuario("76561002", "271590")


def menu():
    print("\n" + "=" * 50)
    print("BIBLIOTECA STEAM — MENÚ")
    print("=" * 50)
    print("── CATÁLOGO ──────────────────────────────────")
    print("  1. Agregar juego al catálogo")
    print("  2. Buscar juego por título")
    print("  3. Buscar juegos por género")
    print("  4. Listar catálogo completo")
    print("── USUARIOS ──────────────────────────────────")
    print("  5. Registrar usuario")
    print("  6. Listar usuarios")
    print("  7. Ver biblioteca de un usuario")
    print("  8. Agregar juego a biblioteca de usuario")
    print("── ───────────────────────────────────────────")
    print("  0. Salir")
    print("=" * 50)


def main():
    catalogo = Catalogo()
    print("\nBienvenido a BibliotecaSteam")
    cargar_datos_prueba(catalogo)

    while True:
        menu()
        opcion = input("Seleccione una opción: ").strip()

        # ── CATÁLOGO ──────────────────────────────────────────────────────────
        if opcion == "1":
            print("\n── Agregar Juego ──")
            app_id       = input("App ID: ").strip()
            titulo       = input("Título: ").strip()
            genero       = input("Género: ").strip()
            desarrollador = input("Desarrollador: ").strip()
            anio_str     = input("Año de lanzamiento: ").strip()
            precio_str   = input("Precio (USD): ").strip()

            try:
                anio   = int(anio_str)
                precio = float(precio_str)
            except ValueError:
                print(" Año o precio inválido.")
                continue

            catalogo.agregar_juego(Juego(app_id, titulo, genero, desarrollador, anio, precio))

        elif opcion == "2":
            termino = input("\nIngresá parte del título: ").strip()
            resultados = catalogo.buscar_juegos_por_titulo(termino)
            if resultados:
                print(f"\n{len(resultados)} resultado(s) encontrado(s):")
                for j in resultados:
                    print(j)
            else:
                print(" No se encontraron juegos con ese título.")

        elif opcion == "3":
            genero = input("\nIngresá el género a buscar: ").strip()
            resultados = catalogo.buscar_juegos_por_genero(genero)
            if resultados:
                print(f"\n{len(resultados)} juego(s) en el género '{genero}':")
                for j in resultados:
                    print(j)
            else:
                print(f" No hay juegos del género '{genero}'.")

        elif opcion == "4":
            catalogo.listar_catalogo()

        # ── USUARIOS ──────────────────────────────────────────────────────────
        elif opcion == "5":
            print("\n── Registrar Usuario ──")
            steam_id = input("Steam ID: ").strip()
            nombre   = input("Nombre de usuario: ").strip()
            catalogo.registrar_usuario(Usuario(steam_id, nombre))

        elif opcion == "6":
            catalogo.listar_usuarios()

        elif opcion == "7":
            steam_id = input("\nSteam ID del usuario: ").strip()
            catalogo.listar_biblioteca_usuario(steam_id)

        elif opcion == "8":
            steam_id = input("\nSteam ID del usuario: ").strip()
            app_id   = input("App ID del juego: ").strip()
            catalogo.agregar_juego_a_usuario(steam_id, app_id)

        elif opcion == "0":
            print("\n ¡Hasta la próxima, gamer!")
            break

        else:
            print(" Opción inválida. Intentá de nuevo.")


if __name__ == "__main__":
    main()
