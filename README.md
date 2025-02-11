# Proyecto-2025A

> Base del proyecto para dar desarrollo a estrategias más elaboradas.

Para el correcto uso del aplicativo se buscará lo siguiente:
El alumnado se conformará por grupos de desarrollo de forma que puedan usar el aplicativo base para desarrollar sus estrategias de forma independiente con su información segura en una rama propia para el desarrollo (`dev`). A su vez, podrán recibir actualizaciones del proyecto principal (`main`) mediante `git pull origin main` mientras sea necesario.

Para lograr esto, primero vamos a realizar un **Fork** al repositorio usando un nombre de preferencia según el equipo de desarrollo. Procederemos a clonar dicho fork en nuestro ordenador mediante `git clone https://github.com/<grupo-usuario>/<Fork-Proyecto-2025A> .` usando GIT, tras esto podremos asociar este repo **local** del equipo con el original para recibir actualizaciones, se logras mediante el comando 
```bash
git remote add upstream https://github.com/Complexum/Proyecto-2025A.git
```
 De forma tal que siempre que estés sobre la rama **`dev`** al aplicar el comando `git pull` o `git fetch upstream` recibirás las actualizaciones ocurridas en `dev`, y a su vez podrás subir código al fork para trabajar en colaborativo.

---

## Instalación

Guía de Configuración del Entorno con VSCode

### ⚙️ Instalación - Configuración

#### 📋 **Requisitos Mínimos**
- ![PowerShell](https://img.shields.io/badge/-PowerShell-blue?style=flat-square) Terminal PowerShell/Bash.
- ![VSCode](https://img.shields.io/badge/-VSCode-007ACC?logo=visualstudiocode&style=flat-square) Visual Studio Code instalado.
- ![Python](https://img.shields.io/badge/-Python%203.10.5-3776AB?logo=python&style=flat-square) Versión python 3.10.5 (o similar).

---

#### 🚀 **Configuración**

1. **🔥 Crear Entorno Virtual**  
   - Abre VSCode y presiona `Ctrl + Shift + P`.
   - Busca y selecciona:  
     `Python: Create Environment` → `Venv` → `Python 3.10.5 64-bit` y si es el de la `(Microsoft Store)` mejor. En este paso, es usualmente recomendable el hacer instalación del Virtual Environment mediante el archivo de requerimientos, no obstante si deseas jugartela a una instalación más eficiente y controlada _(no aplica a todos)_, puedes usar UV. Esto 
   - ![Wait](https://img.shields.io/badge/-ESPERA_5_segundos-important) Hasta que aparezca la carpeta `.venv`

2. **🔄 Reinicio**
   - Cierra y vuelve a abrir VSCode (obligado ✨).
   - Verifica que en la terminal veas `(.venv)` al principio  
     *(Si no: Ejecuta `.\.venv\Scripts\activate` manualmente, pon `activate.bat` si estás en Bash)*


> **💣 (Opcional) Instalación de librerías con UV**
>   En la terminal PowerShell (.venv activado): 
>   Primero instalamos `uv` con 
>   ```powershell
>   pip install uv
>   ```
>   Procedemos a instalar las librerías con
>   ```powershell
>   python -m uv pip install -e .
>   ```

> **Este comando:**
> Instala dependencias de pyproject.toml
> Configura el proyecto en modo desarrollo (-e)
> Genera proyecto_2025a.egg-info con metadatos

> 1. ✅ Verificación Exitosa
   ✔️ Sin errores en terminal
   ✔️ Carpeta proyecto_2025a.egg-info creada
   ✔️ Posibilidad de importar dependencias desde Python

> 🔥 Notas Críticas
   - Procura usar la PowerShell como terminal predeterminada (o Bash).
   - Activar entorno virtual antes de cualquier operación.
   - Si usaste UV la carpeta `proyecto_2025a.egg-info` es esencial.

---

*Para proceder con una introducción o guía de uso del aplicativo, dirígete a `.docs\application.md`, donde encontrarás cómo realizar análisis en este FrameWork.*
