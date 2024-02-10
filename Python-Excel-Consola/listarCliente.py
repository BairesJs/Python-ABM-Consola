#!/usr/bin/env python3
import pandas as pd
from tabulate import tabulate

def mostrar_excel_tabla():
    archivo_excel = "db.xlsx"
    try:
        df = pd.read_excel(archivo_excel)

        # Imprimir la tabla tabulada
        print(tabulate(df, headers='keys', tablefmt='fancy_grid'))

    except FileNotFoundError:
        print("Archivo no encontrado.")

def listado_clientes():
    mostrar_excel_tabla()
    input()

if __name__ == "__main__":
    listado_clientes()
