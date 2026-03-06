import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from src.services.tarea_service import (
    agregar_tarea, completar_tarea, eliminar_tarea, listar_tareas
)

def setup_function():
    import src.services.tarea_service as service
    service.tareas = []
    service.contador_id = 1

def test_agregar_tarea():
    ok, msg = agregar_tarea("Test tarea")
    assert ok == True
    assert "✅" in msg
    assert "Tarea #1" in msg

def test_agregar_tarea_invalida():
    ok, msg = agregar_tarea("ab")
    assert ok == False
    assert "❌" in msg

def test_completar_tarea():
    agregar_tarea("Tarea para completar")
    ok, msg = completar_tarea("1")
    assert ok == True
    assert "✅" in msg

def test_completar_tarea_ya_completada():
    agregar_tarea("Tarea para completar")
    completar_tarea("1")
    ok, msg = completar_tarea("1")
    assert ok == False
    assert "⚠️" in msg

def test_eliminar_tarea():
    agregar_tarea("Tarea para eliminar")
    ok, msg = eliminar_tarea("1")
    assert ok == True
    assert "🗑️" in msg