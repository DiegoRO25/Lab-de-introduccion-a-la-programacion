# 🐍 Creación de un Entorno Virtual en Python (Windows)

Este instructivo documenta paso a paso cómo crear, activar y utilizar un **entorno virtual (`venv`) en Python** usando **Windows, PowerShell y VS Code**, incluyendo **capturas reales del proceso**.

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

## 📁 1. Ubicación del proyecto

Primero, nos movemos a la carpeta donde trabajaremos el proyecto.

```powershell
cd Desktop
cd "Introduccion programacion"
```

📸 **Captura – Ubicación del proyecto en la terminal:**

![Ubicación del proyecto](https://github.com/user-attachments/assets/732af662-72ce-4c1f-abab-30a9a3271407)

---

## 🧱 2. Crear el entorno virtual

Desde la carpeta del proyecto, ejecutamos:

```powershell
python -m venv env
```

Esto crea una carpeta llamada:
```
env/
```

📸 **Captura – Entorno virtual creado correctamente:**

![Creación del entorno virtual](https://github.com/user-attachments/assets/fa617869-8e33-4682-baff-1ac5ec9657af)

---

## 🔐 3. Permitir ejecutar scripts (solo la primera vez)

En Windows, PowerShell bloquea scripts por seguridad.  
Abrimos **PowerShell como Administrador** y ejecutamos:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Confirmamos escribiendo:
```
Y
```

---

## ▶️ 4. Activar el entorno virtual

De regreso en la carpeta del proyecto:

```powershell
env\Scripts\activate
```

Si todo es correcto, el entorno aparece activo en la terminal:

```
(env) PS C:\Users\...
```

📸 **Captura – Entorno virtual activo:**

![Entorno virtual activo](https://github.com/user-attachments/assets/ce57f71c-b2eb-4876-af65-66a1759d3bc4)

---

## 📦 5. Instalar librerías dentro del entorno

Ejemplo con `numpy`:

```powershell
pip install numpy
```

Verificar instalación:
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

#### Dentro de un archivo `.py`
```python
import numpy as np

a = np.array([1, 2, 3])
print(a)
```

Ejecutar:
```powershell
python archivo.py
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

---

## 📂 8. Ignorar el entorno virtual en Git

Crear un archivo `.gitignore` y agregar:
```gitignore
env/
```

---

## 🧪 9. Comprobación final

```powershell
where python
```

Debe apuntar a:
```
...\Introduccion programacion\env\Scripts\python.exe
```

---

## ✅ Conclusión

- El entorno virtual permite trabajar de forma ordenada y profesional  
- Las librerías se instalan solo para el proyecto  
- Es una práctica esencial en el desarrollo con Python  

🚀 **Entorno virtual configurado correctamente y documentado con evidencias visuales**
