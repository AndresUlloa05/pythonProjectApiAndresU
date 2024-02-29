from API.obtener_info_covid import obtener_info_covid
from UI.mostrar_datos import mostrar_datos


def main():

    limite_registros = int(input("Por favor, ingrese el número de registros que desea consultar: "))
    nombre_departamento = input("Ingrese el nombre del departamento que desea consultar: ")

    data_frame = obtener_info_covid(limite_registros, nombre_departamento.upper())

    mostrar_datos(data_frame)


if __name__ == "__main__":
    main()
