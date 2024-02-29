from tabulate import tabulate

def mostrar_datos(data_frame):
    lista_columnas = ["ciudad_municipio_nom", "departamento_nom", "edad", "fuente_tipo_contagio", "estado", "sexo"]
    print(tabulate(data_frame[lista_columnas], tablefmt="pretty", headers=["Numero de registro", "Ciudad de ubicación", "Departamento", "Edad", "Tipo", "Estado", "Sexo"]))

