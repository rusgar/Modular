# Validaciones ESPECÍFICAS de la app de tareas
from utils.validadores.comunes import validar_id  # Reutilizamos

def validar_descripcion(descripcion):
    """La descripción no puede estar vacía ni ser muy corta."""
    descripcion = descripcion.strip()
    if len(descripcion) < 3:
        return False, "La tarea debe tener al menos 3 caracteres."
    if len(descripcion) > 200:
        return False, "La tarea es demasiado larga (máx 200 caracteres)."
    return True, descripcion

def validar_fecha_vencimiento(fecha):
    # Validación específica de tareas
    pass