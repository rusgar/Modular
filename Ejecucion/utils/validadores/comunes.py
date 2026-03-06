# Validaciones que sirven para CUALQUIER app
def validar_id(valor):
    """El ID debe ser un número entero positivo."""
    try:
        id_ = int(valor)
        if id_ <= 0:
            raise ValueError
        return True, id_
    except ValueError:
        return False, "El ID debe ser un número entero positivo."

def validar_email(email):
    # Podría venir en el futuro
    pass

def validar_telefono(telf):
    # Podría venir en el futuro
    pass