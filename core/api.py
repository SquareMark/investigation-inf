import requests
import pandas as pd
import json

def datos_demograficos(perfil):
    url = "https://instagram-statistics-api.p.rapidapi.com/community"

    querystring = {"url": perfil}
    print(perfil)

    headers = {
        "X-RapidAPI-Key": "f104323bd2mshf25ae6828cdd5c3p17ce63jsn441e4323d851",
        "X-RapidAPI-Host": "instagram-statistics-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    json_data = response.json()

    if "data" in json_data:
        data = json_data["data"]
        if isinstance(data, dict):
            datos_demograficos = {
                "paises": [],
                "ciudades": [],
                "generos": [],
                "edades": []
            }

            # Países
            for pais in data["countries"]:
                datos_demograficos["paises"].append({"name": pais["name"], "percent": pais["percent"]})

            # Ciudades
            for ciudad in data["cities"]:
                datos_demograficos["ciudades"].append({"name": ciudad["name"], "percent": ciudad["percent"]})

            # Géneros
            for genero in data["genders"]:
                datos_demograficos["generos"].append({"name": genero["name"], "percent": genero.get("percent", "-")})

            # Edades
            for edad in data["ages"]:
                datos_demograficos["edades"].append({"name": edad["name"], "percent": edad["percent"]})

            # Devolver el diccionario JSON
            #json_string = json.dumps(datos_demograficos, indent=None)
            #return json_string.replace('"', '')
            return datos_demograficos
        else:
            print("Error: La clave 'data' no es un diccionario.")
    else:
        print("Error: La clave 'data' no está presente en el JSON.")
