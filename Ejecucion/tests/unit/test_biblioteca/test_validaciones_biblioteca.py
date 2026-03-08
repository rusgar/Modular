import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from utils.validadores.biblioteca.validaciones_biblioteca import validar_titulo

def test_validar_titulo_correcto():
    assert validar_titulo("1984")

def test_validar_titulo_incorrecto():
    assert not validar_titulo("")