#!/usr/bin/env python3
import pandas as pd

def eliminar_registro():
    # Obtener el ID a eliminar del usuario
    id_a_eliminar = int(input("Ingrese el ID a eliminar: "))

    # Leer el archivo Excel y verificar si el ID existe en el DataFrame
    try:
        df = pd.read_excel("db.xlsx")
        if id_a_eliminar in df['id'].values:
            # Eliminar la fila correspondiente al ID
            df.drop(df[df['id'] == id_a_eliminar].index, inplace=True)

            # Guardar el DataFrame actualizado en el archivo Excel
            with pd.ExcelWriter("db.xlsx", engine="openpyxl", mode="w") as writer:
                df.to_excel(writer, index=False)

            print(f"Registro con ID {id_a_eliminar} eliminado.")
        else:
            print(f"No existe un registro con el ID {id_a_eliminar}.")
    except FileNotFoundError:
        print("No se encontró la base de datos.")

# Llamar a la función para ejecutar la eliminación de registros
#eliminar_registro()
