import requests
import json

# Datos del gobierno de España
# https://opendata.esri.es/
# https://datos.gob.es/en/catalogo/e05024301-precio-de-carburantes-en-las-gasolineras-espanolas
# https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/help
# Datos abiertos de la Comunidad de Madrid:
# https://datos.comunidad.madrid/catalogo/dataset

peticion = requests.get("https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres")
contenido = json.loads(peticion.content)
#print(contenido)  # imprime un fichero JSON enorme
print(contenido["Fecha"]) # muestra que el fichero se actualiza continuamente. Info en tiempo real
listaEstaciones = contenido["ListaEESSPrecio"]
print("Nº estaciones de servicio en España", len(listaEstaciones))

provincia = "Madrid"                                       # si ponemos España busca en toda España
producto = "Precio Gasoleo A"
#producto = "Precio Biodiesel"
#producto = "Precio Gasolina 98 E5"
estacionPrecioMasBajo = {}                                 # INICIALIZAMOS UN DICCIONARIO
for estacion in listaEstaciones:
    if provincia == "España":                              # Se escribe en capitalize
        if estacion[producto] != "":                       # no todas las gasolineras tienen Biodiesel, por ejemplo, asi las quitamos
            if estacionPrecioMasBajo == {}:
                estacionPrecioMasBajo = estacion
            else:
                if estacion[producto] < estacionPrecioMasBajo[producto]:
                    estacionPrecioMasBajo = estacion
    elif provincia.upper() == estacion["Provincia"]:         # filtramos por provincia
        if estacion[producto] != "":
            if estacionPrecioMasBajo == {}:
                estacionPrecioMasBajo = estacion
            else:
                if estacion[producto] < estacionPrecioMasBajo[producto]:
                    estacionPrecioMasBajo = estacion
print(estacionPrecioMasBajo["Rótulo"])                          # mostramos el rótulo de la gasolinera
print(estacionPrecioMasBajo["Dirección"], estacionPrecioMasBajo["C.P."], estacionPrecioMasBajo["Localidad"])
print(estacionPrecioMasBajo[producto], "€/l")
