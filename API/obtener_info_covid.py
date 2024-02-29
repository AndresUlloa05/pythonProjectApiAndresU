
import pandas as pd
from sodapy import Socrata


def obtener_info_covid(lim, area):
    cliente_api = Socrata("www.datos.gov.co", None)
    resultados_api = cliente_api.get("gt2j-8ykr", limit=lim, departamento_nom=area)
    return pd.DataFrame.from_records(resultados_api)

