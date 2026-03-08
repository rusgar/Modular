
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from src.services.biblioteca_service import Biblioteca

def test_agregar_libro():
    service = Biblioteca()
    service.agregar_libro("1984", "Orwell")

    assert len(service.libros) == 1