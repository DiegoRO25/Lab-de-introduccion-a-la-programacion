# 🐍 Instructivo: Creación de un entorno virtual en Python

Este documento explica **paso a paso** cómo crear, activar y utilizar un **entorno virtual en Python**, con el fin de mantener las dependencias del proyecto organizadas y aisladas.

Todas las **capturas de pantalla** utilizadas como referencia se encuentran en la carpeta `Assets` de este repositorio.

---

## 📌 ¿Qué es un entorno virtual?

Un **entorno virtual** es un espacio aislado que permite instalar librerías de Python sin afectar otros proyectos ni la instalación global de Python en el sistema.

---

## 🛠️ 1. Verificar que Python esté instalado

En la terminal, ejecuta:

```bash
python --version
```

o:

```bash
python3 --version
```

---

## 📂 2. Ubicarse en la carpeta del proyecto

```bash
cd ruta/a/tu/proyecto
```

Ejemplo:

```bash
cd Lab-de-introduccion-a-la-programacion
```

---

## 🧪 3. Crear el entorno virtual

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv`.

---

## ▶️ 4. Activar el entorno virtual

### Windows

```powershell
.\venv\Scripts\activate
```

### macOS / Linux

```bash
source venv/bin/activate
```

---

## 📦 5. Instalar librerías

```bash
pip install nombre-del-paquete
```

Ejemplo:

```bash
pip install numpy
```

---


## ⛔ 6. Desactivar el entorno virtual

```bash
deactivate
```

---

## 🚫 7. Evitar subir el entorno a GitHub

Agrega esto a tu `.gitignore`:

```gitignore
venv/
```

---

## ✅ Conclusión

El uso de entornos virtuales es una buena práctica fundamental en Python para mantener proyectos organizados y reproducibles.
