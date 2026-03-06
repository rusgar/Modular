import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__))) 

from src.services.tarea_service import (
    agregar_tarea, completar_tarea, eliminar_tarea, listar_tareas
)

def menu():
    agregar_tarea("Comprar leche")
    agregar_tarea("Estudiar Python")
    agregar_tarea("Hacer ejercicio")

    while True:
        print("\n╔══════════════════════════╗")
        print("║       TODO  LIST         ║")
        print("╠══════════════════════════╣")
        print("║ 1. Añadir tarea          ║")
        print("║ 2. Completar tarea       ║")
        print("║ 3. Eliminar tarea        ║")
        print("║ 4. Ver tareas            ║")
        print("║ 0. Salir                 ║")
        print("╚══════════════════════════╝")

        op = input("  Opción: ").strip()

        if op == "0":
            print("  👋 ¡Hasta luego!")
            break
        elif op == "1":
            desc = input("  Descripción: ")
            _, msg = agregar_tarea(desc)
            print(f"  {msg}")
        elif op == "2":
            id_str = input("  ID de la tarea: ")
            _, msg = completar_tarea(id_str)
            print(f"  {msg}")
        elif op == "3":
            id_str = input("  ID a eliminar: ")
            _, msg = eliminar_tarea(id_str)
            print(f"  {msg}")
        elif op == "4":
            print(listar_tareas())
        else:
            print("  ⚠️ Opción no válida.")