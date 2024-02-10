#!/usr/bin/env python3
import os
from altaCliente import contenido_alta_cliente
from bajaCliente import eliminar_registro
from modificarCliente import contenido_editar_cliente
from listarCliente import listado_clientes

# Funciones para las opciones del menú
def alta_cliente():
    contenido_alta_cliente()
    
def baja_cliente():
    eliminar_registro()
    input()

def modificacion_cliente():
    contenido_editar_cliente()
    input()

def lista_cliente():
    listado_clientes()
    input()

# Crear un menú
def mostrar_menu():
    #os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    print(" Menú de Clientes:")
    print("")
    print(" 1: Alta de Cliente  |  2: Baja de Cliente  |  3: Modificación de Cliente  |  4: Listado de Clientes  |  5: Salir")
    print("")

# Bucle principal
while True:
    mostrar_menu()
    opcion = input(" Seleccione una opción: ")
    print("")

    if opcion == "1":
        alta_cliente()
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
        
    elif opcion == "2":
        baja_cliente()
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    elif opcion == "3":
        modificacion_cliente()
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    elif opcion == "4":
        lista_cliente()
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la pantalla
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
