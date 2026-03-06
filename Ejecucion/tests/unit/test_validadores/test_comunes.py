import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from utils.validadores.comunes import validar_id

def test_validar_id_correcto():
    # IDs válidos
    assert validar_id("1") == (True, 1)
    assert validar_id("999") == (True, 999)
    assert validar_id("1000") == (True, 1000)

def test_validar_id_incorrecto():
    # IDs inválidos
    assert validar_id("0") == (False, "El ID debe ser un número entero positivo.")
    assert validar_id("-5") == (False, "El ID debe ser un número entero positivo.")
    assert validar_id("abc") == (False, "El ID debe ser un número entero positivo.")
    assert validar_id("") == (False, "El ID debe ser un número entero positivo.")
    assert validar_id("12.5") == (False, "El ID debe ser un número entero positivo.")