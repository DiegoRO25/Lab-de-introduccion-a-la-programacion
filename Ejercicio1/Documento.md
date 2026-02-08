# 🐍 Creación de un Entorno Virtual en Python (Windows)

Este instructivo explica paso a paso cómo crear, activar y usar un **entorno virtual (`venv`) en Python** utilizando **Windows, PowerShell y VS Code**.

---

## 📌 ¿Qué es un entorno virtual?
Un entorno virtual es un espacio aislado donde Python instala librerías **solo para un proyecto**, evitando conflictos con otros proyectos o con el sistema global.

---

## ✅ Requisitos
- Windows
- Python 3.3 o superior
- PowerShell
- VS Code (recomendado)

Verificar instalación de Python:
```powershell
python --version
```

---

## 📁 1. Entrar a la carpeta del proyecto
```powershell
cd Desktop
cd "Introduccion programacion"
```

O en una sola línea:
```powershell
cd "C:\Users\TU_USUARIO\Desktop\Introduccion programacion"
```

---

## 🧱 2. Crear el entorno virtual
```powershell
python -m venv env
```

Esto creará una carpeta llamada:
```
env/
```

---

## 🔐 3. Permitir ejecutar scripts (solo la primera vez)

Abrir **PowerShell como Administrador** y ejecutar:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Cuando pregunte, escribir:
```
Y
```
y presionar **Enter**.

---

## ▶️ 4. Activar el entorno virtual
Desde la carpeta del proyecto:
```powershell
env\Scripts\activate
```

Si ves algo como esto, el entorno está activo:
```
(env) PS C:\Users\...
```

---

## 📦 5. Instalar librerías dentro del entorno
Ejemplo con `numpy`:
```powershell
pip install numpy
```

Verificar que esté instalada:
```powershell
pip show numpy
```

---

## 🧠 6. Uso correcto de numpy

### ❌ Incorrecto (en PowerShell):
```powershell
import numpy as np
```

### ✅ Correcto (en Python):

#### Opción A: Dentro de un archivo `.py`
```python
import numpy as np

a = np.array([1, 2, 3])
print(a)
```

Ejecutar el archivo:
```powershell
python archivo.py
```

#### Opción B: Consola interactiva
```powershell
python
```

Luego:
```python
import numpy as np
np.array([1, 2, 3])
```

Salir:
```python
exit()
```

---

## 📄 7. Crear archivos desde la terminal (PowerShell)

Crear un archivo vacío:
```powershell
New-Item main.py
```

Crear archivo con contenido:
```powershell
Set-Content main.py "print('Hola mundo')"
```

Agregar contenido a un archivo existente:
```powershell
Add-Content main.py "print('Otra línea')"
```

---

## 📂 8. Crear carpetas
```powershell
mkdir scripts
```

---

## 🧹 9. Ignorar el entorno virtual en Git
Crear un archivo `.gitignore` y agregar:
```gitignore
env/
```

---

## 🧪 10. Comprobación final
```powershell
where python
```

Debe mostrar una ruta similar a:
```
...\Introduccion programacion\env\Scripts\python.exe
```

---

## ✅ Conclusión
- Los entornos virtuales permiten trabajar de forma organizada
- Las librerías se instalan solo para cada proyecto
- Es una práctica esencial en proyectos reales de Python

🚀 ¡Entorno virtual configurado correctamente!
