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
