#!/usr/bin/env python3
import pandas as pd
from openpyxl import load_workbook

def contenido_alta_cliente():
    # Variable para almacenar el último ID utilizado
    ultimo_id = 0

    # Función para agregar información a la base de datos (archivo Excel)
    def agregar_informacion(nombre, direccion, telefono, email):
        nonlocal ultimo_id  # Acceder a la variable en el ámbito superior
        nonlocal df          # Acceder al DataFrame

        # Incrementar el ID
        ultimo_id += 1

        # Crear una nueva fila con la información ingresada
        nueva_fila = pd.DataFrame({"id": [ultimo_id], "nombre": [nombre], "direccion": [direccion],
                                "telefono": [telefono], "email": [email]})

        # Agregar la nueva fila al DataFrame
        df = pd.concat([df, nueva_fila], ignore_index=True)

        # Guardar el DataFrame actualizado en el archivo Excel
        with pd.ExcelWriter("db.xlsx", engine="openpyxl", mode="w") as writer:
            df.to_excel(writer, index=False)

        print("Información agregada a la base de datos.")

    # Leer el archivo Excel existente o crearlo si no existe
    try:
        df = pd.read_excel("db.xlsx")
        # Obtener el último ID utilizado
        if not df.empty:
            ultimo_id = df['id'].max()
    except FileNotFoundError:
        df = pd.DataFrame(columns=["id", "nombre", "direccion", "telefono", "email"])
        ultimo_id = 0

    print("Ingrese la información del cliente:")

    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    agregar_informacion(nombre, direccion, telefono, email)

# Llamar a la función para ejecutar el contenido
#contenido_alta_cliente()
