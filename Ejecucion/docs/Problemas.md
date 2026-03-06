### SOLUCION DE ERRROES

## Creacion de carpetas __ini__.py

# Crea __init__.py en cada carpeta:
echo "" > utils/__init__.py
echo "" > src/__init__.py
echo "" > test/__init__.py

# Ejecuta el archivo como módulo (no como script suelto):

Termnial:
python -m src.tareas_app

## ERROR: ModuleNotFoundError: No module named 'services'

**Causa:** Falta el archivo `__init__.py` en la carpeta `services/`

**Solución:**
1. Crea un archivo vacío llamado `__init__.py` en `src/services/`
2. Python necesita este archivo para reconocer la carpeta como un "paquete"
3. ¡No necesita contenido! El archivo vacío es suficiente

**Regla de oro:** 
Toda carpeta que contenga archivos .py que importes DEBE tener un `__init__.py`

## ERROR: ModuleNotFoundError: No module named 'services'

**Causa:** Python busca módulos en la raíz del proyecto, pero 'services' está dentro de 'src/'.

**Solución 1:** Usar la ruta completa en el import
```python
from src.services.tarea_service import ...

```

## Solución 2: Añadir 'src' al path de búsqueda

```python
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
```
 # ¿Por qué pasa?

Python busca módulos en las carpetas listadas en '''sys.path'''

La carpeta src/ NO está en sys.path por defecto

Cuando hacemos from services import..., Python busca services en la raíz, pero está dentro de src/

Regla de oro:
Siempre importa desde la raíz del proyecto: from src.services... o from utils...