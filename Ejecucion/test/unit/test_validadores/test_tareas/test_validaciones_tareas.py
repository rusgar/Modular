
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))

from utils.validadores.tareas.validaciones_tareas import validar_descripcion

def test_validar_descripcion_correcta():
    assert validar_descripcion("Comprar leche") == (True, "Comprar leche")
    assert validar_descripcion("  Estudiar Python  ") == (True, "Estudiar Python")
    assert validar_descripcion("a" * 50) == (True, "a" * 50)

def test_validar_descripcion_incorrecta():
    assert validar_descripcion("") == (False, "La tarea debe tener al menos 3 caracteres.")
    assert validar_descripcion("  ") == (False, "La tarea debe tener al menos 3 caracteres.")
    assert validar_descripcion("ab") == (False, "La tarea debe tener al menos 3 caracteres.")