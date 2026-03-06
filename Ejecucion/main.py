# main.py
from src.tareas_app import menu as menu_tareas
from src.biblioteca_app import menu as menu_biblioteca

if __name__ == "__main__":
    while True:
        print("""
╔══════════════════════════╗
║    APLICACIONES MÓDULO   ║
╠══════════════════════════╣
║ 1. TODO List (Tareas)    ║
║ 2. Biblioteca            ║
║ 0. Salir                 ║
╚══════════════════════════╝
""")
        op = input("  Elige una app: ").strip()
        
        if op == "0":
            print("  👋 ¡Hasta luego!")
            break
        elif op == "1":
            menu_tareas()
        elif op == "2":
            menu_biblioteca()
        else:
            print("  ⚠️ Opción no válida.")