import os

ARCHIVO = "data.dat"
CLAVE = "Kirby64"

def inicio():
    print("Inicio de Sesión")
    intento = input("Ingresa la contraseña: ")
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
if inicio():
    while menu():
        pass