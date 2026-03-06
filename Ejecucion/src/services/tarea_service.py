import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.validaciones import validar_descripcion, validar_id

tareas = []
contador_id = 1

def agregar_tarea(descripcion):
    global contador_id
    ok, resultado = validar_descripcion(descripcion)
    if not ok:
        return False, f"❌ {resultado}"
    tarea = {
        "id": contador_id,
        "descripcion": resultado,
        "completada": False,
    }
    tareas.append(tarea)
    contador_id += 1
    return True, f"✅ Tarea #{tarea['id']} añadida: '{resultado}'"

def completar_tarea(id_str):
    ok, resultado = validar_id(id_str)
    if not ok:
        return False, f"❌ {resultado}"
    for tarea in tareas:
        if tarea["id"] == resultado:
            if tarea["completada"]:
                return False, "⚠️ La tarea ya estaba completada."
            tarea["completada"] = True
            return True, f"✅ Tarea #{resultado} marcada como completada."
    return False, f"❌ No existe ninguna tarea con ID {resultado}."

def eliminar_tarea(id_str):
    ok, resultado = validar_id(id_str)
    if not ok:
        return False, f"❌ {resultado}"
    for i, tarea in enumerate(tareas):
        if tarea["id"] == resultado:
            tareas.pop(i)
            return True, f"🗑️ Tarea #{resultado} eliminada."
    return False, f"❌ No existe ninguna tarea con ID {resultado}."

def listar_tareas():
    if not tareas:
        return "  📭 No hay tareas todavía."
    resultado = []
    resultado.append(f"\n  {'ID':<5} {'ESTADO':<12} DESCRIPCIÓN")
    resultado.append("  " + "─" * 40)
    for t in tareas:
        estado = "✅ Hecha  " if t["completada"] else "⏳ Pendiente"
        resultado.append(f"  {t['id']:<5} {estado:<12} {t['descripcion']}")
    resultado.append("")
    return "\n".join(resultado)