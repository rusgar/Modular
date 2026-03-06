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

## Fase 2.5: Validadores Especializados (NIVEL PRO)

**Archivos creados:**
- `utils/validadores/comunes.py` → Validaciones genéricas
- `utils/validadores/tareas/validaciones_tareas.py` → Validaciones específicas

### Estructura final de validadores:

```
utils/
└── validadores/
    ├── __init__.py
    ├── comunes.py            # validar_id, validar_email, etc.
    └── tareas/
        ├── __init__.py
        └── validaciones_tareas.py   # validar_descripcion
```


### Código ejemplo:
```python
# comunes.py
def validar_id(valor):
    """Válido para TAREAS y BIBLIOTECA"""
    ...

# validaciones_tareas.py
from utils.validadores.comunes import validar_id

def validar_descripcion(descripcion):
    """EXCLUSIVO de la app de tareas"""
    ...

```

### ¿Qué logramos?

✅ Separación total: Cada validación en su lugar

✅ Reutilización: validar_id lo usa TODO

✅ Escalabilidad: Podemos añadir biblioteca/ con sus propias validaciones

✅ Mantenibilidad: Si cambia el formato de ID, solo tocamos comunes.py



---

## 📌 **También actualiza `docs/principios-solid.md`:**

Añade este ejemplo en la sección de **SRP**:

```python
# Ejemplo de Responsabilidad Única en Validaciones

## MAL (Todo junto)
utils/validaciones.py
├── def validar_id()        # Genérico
├── def validar_descripcion() # Específico tareas
├── def validar_titulo()     # Específico biblioteca
└── def validar_autor()      # Específico biblioteca

## BIEN (Separado por responsabilidad)
utils/validadores/
├── comunes.py               # Solo lo GENÉRICO
├── tareas/
│   └── validaciones_tareas.py  # Solo lo de TAREAS
└── biblioteca/
    └── validaciones_biblioteca.py  # Solo lo de BIBLIOTECA
    ```

```
---
 ##  Fase 3: App de Biblioteca Modularizada
    

**Archivos creados:**
- `src/models/libro.py` → Modelo de datos
- `utils/validadores/biblioteca/validaciones_biblioteca.py` → Validaciones específicas
- `src/services/biblioteca_service.py` → Lógica de negocio
- `src/biblioteca_app.py` → Solo menú

**Validaciones reutilizadas:**
- `validar_id` de `comunes.py` (para futuras búsquedas por ID)

**Nuevas validaciones específicas:**
- `validar_titulo()` → Mínimo 2 caracteres
- `validar_autor()` → Mínimo 3 caracteres
- `validar_precio()` → Número positivo
- `validar_cantidad()` → Entero positivo

**Logros:**
- ✅ Misma estructura que app de tareas
- ✅ Validaciones reutilizables
- ✅ Responsabilidad única en cada archivo
- ✅ Menú principal unificado en `main.py`

```