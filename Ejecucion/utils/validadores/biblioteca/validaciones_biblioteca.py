# utils/validadores/biblioteca/validaciones_biblioteca.py
from utils.validadores.comunes import validar_id

def validar_titulo(titulo):
    """Validación específica para títulos de libros"""
    titulo = titulo.strip()
    if len(titulo) < 2:
        return False, "El título debe tener al menos 2 caracteres."
    return True, titulo

def validar_autor(autor):
    """Validación específica para autores"""
    autor = autor.strip()
    if len(autor) < 3:
        return False, "El autor debe tener al menos 3 caracteres."
    return True, autor

def validar_precio(precio_str):
    """Validación específica para precios"""
    try:
        precio = float(precio_str)
        if precio <= 0:
            return False, "El precio debe ser positivo."
        return True, precio
    except ValueError:
        return False, "El precio debe ser un número válido."

def validar_cantidad(cantidad_str):
    """Validación específica para cantidades"""
    try:
        cantidad = int(cantidad_str)
        if cantidad <= 0:
            return False, "La cantidad debe ser positiva."
        return True, cantidad
    except ValueError:
        return False, "La cantidad debe ser un número entero."