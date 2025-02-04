# Proyecto-2025A

Base del proyecto para dar desarrollo a estrategias más elaboradas.

---

## Instalación

Guía de Configuración del Entorno con UV y VSCode

### ⚙️ Instalación - Configuración Express con UV + VSCode

#### 📋 **Requisitos Mínimos**
- ![PowerShell](https://img.shields.io/badge/-PowerShell-blue?style=flat-square) Terminal PowerShell (¡nada de CMD!)
- ![VSCode](https://img.shields.io/badge/-VSCode-007ACC?logo=visualstudiocode&style=flat-square) Visual Studio Code instalado
- ![Python](https://img.shields.io/badge/-Python%203.11.9-3776AB?logo=python&style=flat-square) Versión exacta: 3.11.9

---

#### 🚀 **Configuración**

1. **🔥 Crear Entorno Virtual**  
   - Abre VSCode y presiona `Ctrl + Shift + P`
   - Busca y selecciona:  
     `Python: Create Environment` → `Venv` → `Python 3.11.9 64-bit` y si es el de la `(Microsoft Store)` mejor.
   - ![Wait](https://img.shields.io/badge/-ESPERA_5_segundos-important) Hasta que aparezca la carpeta `.venv`.

2. **🔄 Reinicio**
   - Cierra y vuelve a abrir VSCode (obligado ✨).
   - Verifica que en la terminal veas `(.venv)` al principio  
     *(Si no: ejecuta `.\.venv\Scripts\activate` manualmente)*

3. **💣 Instalación con UV**  
   En la terminal PowerShell (.venv activado):  
   ```powershell
   python -m uv pip install -e .
   ```
2. Este comando:
   - Instala todas las dependencias definidas en `pyproject.toml`
   - Instala el proyecto en modo desarrollo (-e)
   - Crea una carpeta `proyecto_2025a.egg-info` con metadatos del proyecto.

### Verificación
- La instalación es exitosa si:
  - No hay mensajes de error en la terminal.
  - Se crea la carpeta `proyecto_2025a.egg-info`.
  - Puedes importar las dependencias instaladas desde Python.

### Notas Importantes
- Siempre usar PowerShell como terminal predeterminada para consistencia.
- El entorno virtual debe estar activado antes de instalar dependencias.
- La carpeta `proyecto_2025a.egg-info` es normal y necesaria - se puede agregar a `.gitignore`.

### Ejecución del programa

Abres una terminal, escribes `py e` tabulas y das enter, así de simple! Alternativamente escribiendo en terminal `python .\exec.py` deberás ejecutar una muestra del aplicativo para una Red de 04 nodos, generarando un análisis completo sobre la misma, de tal forma que se obtendrán dos artefactos tras la ejecución

Por otro lado puedes realizar un anális específico sobre una red

Al final podemos realizar ejecución desde `py exec` y pasar a corregir los errores de la librería Pyphi (en el documento `.docs\errors.md` encuentras la guía de bolsillo para arreglar estos problemas).

Tras ello podrás realizar distintas pruebas en el aplicativo, por ejemplo, el código por defecto tenemos:

```py
from models.base.manager import Manager

from src.models.logic.phi import Phi
from src.models.logic.force import BruteForce
from src.models.logic.q_nodes import QNodes


def start_up():
    """Punto de entrada principal"""
                   # ABCD
    estado_inicio = "1000"
    sys_config = Manager(estado_inicial=estado_inicio)

    ## Ejemplo de solución mediante fuerza bruta ##

    analizador_fb = BruteForce(sys_config)
    analizador_fb.analizar_completamente_una_red()
```

Podemos ver cómo al definir el estado inicial `1000` estamos usando implícitamente una red de 04 nodos y sólo asignamos al primer nodo _(el A)_ el valor de 1 _(canal activo)_ y los demás _(BCD=000)_ o inactivos, esta estará ubicada en el directorio de `.samples\`, si tenemos varias deeberemos configurar en el `Manager` cuál querremos utilizar manualmente o cambiando la página desde la configuración del aplicativo.

En este lo que hacemos es ejecutar un análsis de forma completa sobre una red, analizando lo que son todos sus posibles sistemas candidatos, por cada uno de ellos sus posibles subsistemas y sobre cada uni hacemos un análisis de irreducibilidad sistémica (SIA), de forma que tendremos tanto la solución de la ejecución como una serie metadatos sobre los que podemos dar un análisis.
Este resultado se ubicará en el directorio `review\resolver\red_ejecutada\estado_inicial\`, donde el sistema candidato será un archivo excel, cada hoja un posible subsistema, cada fila una partición de las variables en tiempo presente $(t_0)$ y las columnas para un tiempo futuro $(t_1)$ de forma que las variables que pertenezcan a un mismo dígito pertenecen a la misma partición.

Primeramente se cuenta con un decorador `@profile` encontrado en `src.middlewares.profile` aplicable sobre cualquier función, este nos permite generar un análisis temporal del llamado de subrutinas, teniendo dos modos de visualización podremos apreciar una vista global (Call Stack) y particular (Timeline). Este decorador nos será especialmente útil para la detección de cuellos de botella durante la ejecución del programa para cualquier subrutina usada, además de permitirnos conocer el uso de CPU y dar uso en procesos de optimización.

Secundariamente sobre el directorio `logs`, cada que se use el objeto `self.logger` en la clase de ejecución se generará un archivo indicando los datos logeados/impresos para hacer un seguimiento completo de la ejecución, este se almacena por carpetas de la forma `dia_mes_año\hora\metodo_del_log` manteniendo un historial de las ejecuciones. Este logger se volverá casual/sospechosamente útil cuando el rastro de las ejecuciones sea _extremandamente_ extenso para algún proceso.


Así mismo si quisieramos hacer más pruebas con un subsistema específico para una red sería con:
```py
def start_up():
    """Punto de entrada principal"""
                   # ABCD #
    estado_inicio = "1000"
    condiciones   = "1110"
    alcance =       "1110"
    mechanismo =    "1110"

    sys_config = Manager(estado_inicial=estado_inicio)

    ### Ejemplo de solución mediante módulo de pyphi ###

    analizador_fb = BruteForce(sys_config)
    sia_uno = analizador_fb.aplicar_estrategia(condiciones, alcance, mechanismO)
    print(sia_uno)
```

Como se aprecia cada variable está asociada con una posición, de forma que las variables a mantener tienen el bit en uno (1), mientras que las que querremos descartar las enviaremos en cero (0).

Por ejemplo una ejecución con Pyphi para una red específica se vería así:

```py
from models.base.manager import Manager

from src.models.logic.phi import Phi


def start_up():
    """Punto de entrada principal"""
                   # ABCD #
    estado_inicio = "1000"
    condiciones =   "1000"
    alcance =       "1110"
    mechanismo =    "1110"

    sys_config = Manager(estado_inicial=estado_inicio)

    ### Ejemplo de solución mediante Pyphi ###

    analizador_fb = Phi(sys_config)
    sia_dos = analizador_fb.aplicar_estrategia(condiciones, alcance, mechanismo)
    print(sia_dos)
```

### Pruebas

En el archivo de pruebas en el directorio `.tests` encontrarás el documento excel con las pruebas a resolver mediante uso del aplicativo.


```py
def start_up():
    """Punto de entrada principal"""
   from src.models.logic.force import BruteForce


                   # ABCD #
    estado_inicio = "1000"
    condiciones__ = "1110"
    alcance______ = "1110"
    mechanismo___ = "1110"

    sys_config = Manager(estado_inicial=estado_inicio)
    ### Ejemplo de solución mediante módulo de pyphi ###

    # pyphi_analyzer = Phi(sys_config)
    # sia_uno = pyphi_analyzer.run(condiciones__, alcance______, mechanismo___)
    # print(sia_uno)

    ### Ejemplo de solución mediante fuerza bruta ###

    bf_analyzer = BruteForce(sys_config)
    # sia_dos = bf_analyzer.run(condiciones__, alcance______, mechanismo___)
    # print(sia_dos)
    bf_analyzer.analizar_completamente_una_red()

    # q_analyzer = QNodes(sys_config)
    # sia_tres = q_analyzer.run(condiciones__, alcance______, mechanismo___)
    # print(sia_tres)
```