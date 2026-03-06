# src/biblioteca_app.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.services.biblioteca_service import Biblioteca
from src.models.libro import Libro

def menu():
    # Datos de prueba
    biblioteca = Biblioteca("Biblioteca Central")
    biblioteca.agregar_libro(Libro("El Quijote", "Cervantes", 15.00, 3))
    biblioteca.agregar_libro(Libro("Cien años", "García Márquez", 12.50, 2))
    biblioteca.agregar_libro(Libro("1984", "Orwell", 10.00, 1))

    while True:
        print("""
╔══════════════════════════╗
║     BIBLIOTECA CENTRAL   ║
╠══════════════════════════╣
║ 1. Prestar libro         ║
║ 2. Devolver libro        ║
║ 3. Comprar libro         ║
║ 4. Vender libro          ║
║ 5. Ver catálogo          ║
║ 0. Salir                 ║
╚══════════════════════════╝
""")

        op = input("  Opción: ").strip()

        if op == "0":
            print("  👋 ¡Hasta luego!")
            break
        elif op == "1":
            titulo = input("  Título: ")
            print(f"  {biblioteca.prestar_libro(titulo)}")
        elif op == "2":
            titulo = input("  Título: ")
            print(f"  {biblioteca.devolver_libro(titulo)}")
        elif op == "3":
            titulo = input("  Título: ")
            autor = input("  Autor: ")
            precio = input("  Precio: ")
            cantidad = input("  Cantidad: ")
            ok, msg = biblioteca.comprar_libro(titulo, autor, precio, cantidad)
            print(f"  {msg}")
        elif op == "4":
            titulo = input("  Título: ")
            print(f"  {biblioteca.vender_libro(titulo)}")
        elif op == "5":
            print(biblioteca.mostrar_catalogo())
        else:
            print("  ⚠️ Opción no válida.")

if __name__ == "__main__":
    menu()