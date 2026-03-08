# 🗂️ Ejecucion — Solución de Referencia

> Esta carpeta contiene la implementación completa del ejercicio de modularización.  
> Úsala para comparar con tu propia solución, entender las decisiones arquitectónicas y aprender cómo se organiza un proyecto Python real.  
> **No copies — compara, entiende y aplica.**

---

## 📌 ¿Qué es este proyecto?

Solución de referencia para la tarea de modularización de aplicaciones Python.  
Contiene dos aplicaciones completamente refactorizadas desde su versión monolítica original:

- **TODO List** — Gestión de tareas (añadir, completar, eliminar, listar)
- **Biblioteca** — Sistema de gestión de libros (prestar, devolver, comprar, vender)

Ambas siguen los principios de **Clean Code** y **arquitectura modular**, separando claramente configuración, datos, modelos, lógica de negocio, validaciones e interfaz de usuario.

---

## 📂 Estructura del proyecto

```
Ejecucion/
│
├── src/                             # Código fuente de ambas aplicaciones
│   ├── config/
│   │   ├── __init__.py
│   │   └── constantes.py            # Constantes compartidas (mensajes, límites, etc.)
│   │
│   ├── data/                        # Datos de ejemplo / seed data
│   │   ├── __init__.py
│   │   ├── biblioteca.py            # Libros de prueba precargados
│   │   └── tareas_ejemplo.py        # Tareas de prueba precargadas
│   │
│   ├── models/                      # Modelos de dominio (entidades)
│   │   ├── __init__.py
│   │   └── libro.py                 # Clase Libro
│   │
│   ├── services/                    # Lógica de negocio
│   │   ├── __init__.py
│   │   ├── biblioteca_service.py    # Operaciones sobre la biblioteca
│   │   └── tarea_service.py         # Operaciones sobre las tareas
│   │
│   ├── __init__.py
│   ├── biblioteca_app.py            # App Biblioteca: menú e interacción con usuario
│   └── tareas_app.py                # App TODO: menú e interacción con usuario
│
├── tests/                           # Tests unitarios organizados por capa
│   └── unit/
│       ├── test_biblioteca/
│       │   ├── test_biblioteca_service.py
│       │   └── test_validaciones_biblioteca.py
│       ├── test_services/
│       │   └── test_tarea_service.py
│       ├── test_validadores/
│       │   └── test_validaciones_tareas.py
│       ├── test_comunes.py
│       └── __init__.py
│
├── utils/                           # Utilidades transversales a ambas apps
│   ├── validadores/
│   │   ├── biblioteca/
│   │   │   ├── __init__.py
│   │   │   └── validaciones_biblioteca.py
│   │   ├── tareas/
│   │   │   ├── __init__.py
│   │   │   └── validaciones_tareas.py
│   │   ├── __init__.py
│   │   └── comunes.py               # Validaciones compartidas entre apps
│   ├── __init__.py
│   └── validaciones.py              # Punto de entrada unificado de validaciones
│
├── docs/
│   └── Problemas.md                 # Registro de problemas encontrados y cómo se resolvieron
│
├── main.py                          # Punto de entrada — lanza el selector de app
├── __init__.py
├── requirements.txt
└── .gitignore
```

---

## ▶️ Cómo ejecutar

### 1. Clona el repositorio

```bash
git clone https://github.com/rusgar/Modular.git
cd Modular/Ejecucion
```

### 2. (Opcional) Crea un entorno virtual

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 3. Instala dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```bash
python main.py
```

---

## 🧪 Tests

```bash
pytest
# o con detalle:
pytest -v
```

Los tests están organizados por capa, en paralelo con `src/` y `utils/`, para que sea fácil localizar qué se está probando en cada momento.

---

## 🧠 Decisiones de diseño — Para entender el porqué

Esta sección es especialmente relevante para los alumnos.

### ¿Por qué tantas capas?

El ejercicio pedía como mínimo separar en 3 archivos. Esta solución va más lejos para mostrar cómo se escala esa idea en proyectos reales:

| Capa | Responsabilidad | Dónde |
|---|---|---|
| **Config** | Constantes y configuración global | `src/config/` |
| **Data** | Datos de prueba separados del código | `src/data/` |
| **Models** | Qué es una entidad (Libro, Tarea) | `src/models/` |
| **Services** | Qué operaciones se pueden hacer | `src/services/` |
| **App (UI)** | Cómo interactúa el usuario | `src/biblioteca_app.py`, `src/tareas_app.py` |
| **Utils/Validadores** | Validaciones reutilizables, separadas por app | `utils/validadores/` |
| **Main** | Solo orquesta, no tiene lógica propia | `main.py` |

### ¿Por qué `utils/validadores/` está fuera de `src/`?

Porque las validaciones son **transversales**: no pertenecen ni a la app de tareas ni a la de biblioteca — las usan ambas. Ponerlas en `utils/` comunica esa intención claramente y evita que una app dependa de la carpeta de la otra.

Además están subdivididas por dominio (`biblioteca/`, `tareas/`) con un `comunes.py` para las reglas compartidas. Eso facilita añadir una tercera app en el futuro sin tocar lo existente.

### ¿Por qué `src/data/` con datos de ejemplo?

Separar los datos de prueba del código de producción es una buena práctica. Si mañana quieres cambiar los libros o tareas que se cargan al inicio, sabes exactamente dónde ir sin tocar la lógica.

### ¿Por qué `docs/Problemas.md`?

Documentar los problemas encontrados durante el desarrollo es tan valioso como el código mismo. Deja trazabilidad de decisiones y enseña a pensar en retrospectiva. En equipos profesionales esto se hace en issues de GitHub o documentos de arquitectura.

### ¿Por qué `main.py` casi no tiene código?

Porque su único trabajo es arrancar la aplicación. Si `main.py` contiene lógica de negocio o validaciones, la modularización está incompleta.

---

## 🔁 Comparativa: antes vs después

| | Versión monolítica (`Tarea/`) | Esta solución (`Ejecucion/`) |
|---|---|---|
| Archivos | 1 por app | Estructura multicapa |
| Líneas por archivo | ~100 | 15–40 por módulo |
| Testeable | ❌ Difícil | ✅ Tests por capa |
| Reutilizable | ❌ No | ✅ `utils/` compartido |
| Mantenible | ❌ A escala | ✅ Cambio localizado |
| Datos separados del código | ❌ No | ✅ `src/data/` |
| `main.py` limpio | ❌ No | ✅ Solo orquesta |

---

## 📋 Criterios del ejercicio cubiertos

| Criterio | Estado |
|---|---|
| Separación clara de responsabilidades | ✅ |
| Uso correcto de `import` | ✅ |
| Funcionalidad idéntica al original | ✅ |
| `main.py` limpio y legible | ✅ |
| Type hints y docstrings | ✅ |
| Estructura de carpetas lógica | ✅ |
| `datos_prueba` separado del código | ✅ (`src/data/`) |
| Tests unitarios organizados por capa | ✅ |
| Documentación del proceso | ✅ (`docs/Problemas.md`) |

---

## ⚠️ Nota técnica — `.vscode/`

La carpeta `.vscode/` contiene configuración local del editor y no debería subirse al repositorio. Asegúrate de que está incluida en `.gitignore`:

```
.vscode/
```

---

## 🛠️ Tecnologías

- Python 3.10+
- pytest

---

*Proyecto educativo — DiCampus · IA Aplicada a la Programación · RUSGAR · Febrero 2026*