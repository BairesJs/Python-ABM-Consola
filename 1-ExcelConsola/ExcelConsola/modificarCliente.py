#!/usr/bin/env python3
import pandas as pd

df = pd.DataFrame(columns=["id", "nombre", "direccion", "telefono", "email"])

def cargar_datos():
    global df
    try:
        df = pd.read_excel("db.xlsx")
    except FileNotFoundError:
        # Si no se encuentra el archivo, se creará uno vacío
        df.to_excel("db.xlsx", index=False)

def contenido_editar_cliente():
    global df

    print("Modificar Registro")
    cargar_datos()

    id_a_modificar = int(input("Introduce el ID a modificar: "))

    registro = df[df['id'] == id_a_modificar]
    if not registro.empty:
        print("Registro encontrado. Puedes modificar la información.")
        nombre = input(f"Nuevo nombre ({registro['nombre'].values[0]}): ") or registro['nombre'].values[0]
        direccion = input(f"Nueva dirección ({registro['direccion'].values[0]}): ") or registro['direccion'].values[0]
        telefono = input(f"Nuevo teléfono ({registro['telefono'].values[0]}): ") or registro['telefono'].values[0]
        email = input(f"Nuevo email ({registro['email'].values[0]}): ") or registro['email'].values[0]

        # Actualizar el registro en el DataFrame
        df.loc[df['id'] == id_a_modificar, 'nombre'] = nombre
        df.loc[df['id'] == id_a_modificar, 'direccion'] = direccion
        df.loc[df['id'] == id_a_modificar, 'telefono'] = telefono
        df.loc[df['id'] == id_a_modificar, 'email'] = email

        df.to_excel("db.xlsx", index=False)

        print("Información modificada en la base de datos.")
    else:
        print(f"No existe un registro con el ID {id_a_modificar}.")

# Llamar a la función para ejecutar la modificación de registros
#contenido_editar_cliente()
