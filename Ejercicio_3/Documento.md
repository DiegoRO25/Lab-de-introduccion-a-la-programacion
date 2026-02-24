# Explicación del Código de Login en Python

## Código original

``` python
intentos = 0
while intentos < 3:
    usuario = input("ingresa tu nombre de usuario: ")
    contraseña = input("ingresa la contraseña: ")
    
    if len(usuario) == 0:
        print ("El nombre de usuario no debe estar vacío") 
        
    if " " in usuario: 
        print ("El nombre de usuario no debe contener espacios")    

    if len(contraseña) < 8:
        print("la contraseña debe tener al menos 8 caracteres")

    if usuario == ("admin") and contraseña == ("Admin2026"): 
        print("Se ingresó correctamente al sistema")
        break
    else:
        intentos += 1
        print(f"Intento número: {intentos}")
```

------------------------------------------------------------------------

## Explicación paso a paso

### 1️⃣ Inicialización del contador

``` python
intentos = 0
```

Se crea una variable llamada `intentos` que comienza en 0.\
Esta variable llevará el control de cuántas veces el usuario ha fallado
al intentar iniciar sesión.

------------------------------------------------------------------------

### 2️⃣ Ciclo while

``` python
while intentos < 3:
```

Este ciclo permite que el usuario tenga un máximo de 3 intentos.\
Mientras el número de intentos sea menor que 3, el programa seguirá
ejecutándose.

------------------------------------------------------------------------

### 3️⃣ Entrada de datos

``` python
usuario = input(...)
contraseña = input(...)
```

El programa solicita al usuario que ingrese:

-   Su nombre de usuario
-   Su contraseña

La función `input()` siempre devuelve texto (string).

------------------------------------------------------------------------

### 4️⃣ Validaciones del usuario

#### Usuario vacío

``` python
if len(usuario) == 0:
```

Verifica si el usuario no escribió nada.

------------------------------------------------------------------------

#### Usuario con espacios

``` python
if " " in usuario:
```

Verifica si el nombre de usuario contiene espacios, lo cual no está
permitido.

------------------------------------------------------------------------

### 5️⃣ Validación de contraseña

``` python
if len(contraseña) < 8:
```

Comprueba que la contraseña tenga al menos 8 caracteres.

------------------------------------------------------------------------

### 6️⃣ Verificación de credenciales

``` python
if usuario == ("admin") and contraseña == ("Admin2026"):
```

Aquí se compara:

-   Que el usuario sea exactamente `"admin"`
-   Que la contraseña sea exactamente `"Admin2026"`

El operador `and` exige que ambas condiciones sean verdaderas.

Si ambas coinciden:

-   Se imprime un mensaje de acceso correcto.
-   Se usa `break` para salir del ciclo inmediatamente.

------------------------------------------------------------------------

### 7️⃣ Intento fallido

``` python
else:
    intentos += 1
```

Si las credenciales no coinciden:

-   Se incrementa el contador de intentos.
-   Se muestra en qué número de intento va el usuario.

------------------------------------------------------------------------

## 🎯 Conclusión

Este código demuestra el uso de:

-   Variables
-   Ciclos `while`
-   Condicionales `if`
-   Operadores lógicos (`and`)
-   Contador de intentos
-   Uso de `break`

Es un buen ejercicio para practicar control de flujo y validación básica
en Python.
