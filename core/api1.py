import requests
import pandas as pd
import json

def view_profile(perfil):  # Cambiamos "profile" a "perfil" para usar un término en español
	url = "https://instagram-statistics-api.p.rapidapi.com/community"

	querystring = {"url": perfil}

	headers = {
		"X-RapidAPI-Key": "f104323bd2mshf25ae6828cdd5c3p17ce63jsn441e4323d851",
		"X-RapidAPI-Host": "instagram-statistics-api.p.rapidapi.com"
	}

	response = requests.get(url, headers=headers, params=querystring)

	# Extrae los datos JSON de la respuesta
	json_data = response.json()

    # Mapa de traducción de las cabeceras de inglés a español
	translation_map = {
        "url": "URL",
        "name": "Nombre",
        "description": "Descripción",
        "screenName": "Username",
        "usersCount": "Conteo de Usuarios",
        "verified": "Verificado",
        "avgER": "Promedio ER",
        "avgInteractions": "Promedio Interacciones",
        "avgViews": "Promedio Vistas",
        "ratingIndex": "Indice de Clasificación",
        "qualityScore": "Puntuación de Calidad",
        "avgLikes": "Promedio MeGustas",
        "avgComments": "Promedio Comentarios",
        "country": "País",
        "countryCode": "Código País",
        "city": "Ciudad",
        "type": "Tipo",
        "gender": "Género",
        "age": "Edad",
        "categories": "Categorías",
        "contactEmail": "Email de Contacto",
        "audienceSeverity": "Severidad de Audiencia"
    }

	data_to_process = json_data['data']
 	# Traducir las cabeceras solo si están en el mapa de traducción
	translated_data = {}
	for k, v in data_to_process.items():
		if k in translation_map:
			translated_key = translation_map[k]
			translated_data[translated_key] = v
			
    # Convertir el diccionario a JSON
	#json_data = json.dumps(translated_data, indent=4)

    # Retornar el JSON
	return translated_data

