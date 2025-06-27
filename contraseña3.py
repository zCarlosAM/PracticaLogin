import os
import pwinput

CLAVE = "Kirby64"

def agregar_usuario(usuario, clave):
    with open("usuarios.txt", "a") as archivo:
        archivo.write(f"{usuario},{clave}\n")

def cargar_usuarios():
    usuarios = {}
    if os.path.exists("usuarios.txt"):
        with open("usuarios.txt", "r") as archivo:
            for linea in archivo:
                usuario, clave = linea.strip().split(",")
                usuarios[usuario] = clave
    return usuarios

def inicio():
    agregar_usuario("Admin", CLAVE)
    usuarios = cargar_usuarios()
    print("Inicio de Sesión")

    usuario = input("Usuario: ")

    intento = pwinput.pwinput(prompt='Contraseña: ', mask='*')
    if usuario in usuarios and usuarios[usuario] == intento:
        print("Acceso permitido\n")
        return True
    else:
        print("Usuario o contraseña incorrectos.\n")
        return False

    if intento == CLAVE:
        print("Acceso permitido\n")
        return True
    else:
        print("Contraseña incorrecta")
        return False

def menu():
    os.system('cls || clear')
    print("MENU")
    print("1. Hacer algo")
    print("2. Hacer otra cosa")
    print("3. Hacer una cosa muy misteriosa")
    print("4. Salir")
    
    opcion = input("\nEscoja una opción: ")
    os.system('cls || clear')
    
    if opcion == "4":
        print("Bye bye!")
        return False
    else:
        print("Funcion no implementada.")
        input("\nPulse cualquier tecla para continuar. ")
        return True

os.system('cls || clear')

intentos = 0
while intentos < 3:
    if inicio():
        intentos = 3
        while menu():
            pass
    else:
        intentos += 1