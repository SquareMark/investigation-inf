import requests
import pandas as pd
import json

def view_posts(perfil): 
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
        "date": "Fecha",
        "type": "Tipo",
        "image": "Media",
        "likes": "Likes",
        "comments": "Comentarios",
        "text": "Texto"
    }

	data_to_process = json_data['data']['lastPosts']
 	# Traducir las cabeceras solo si están en el mapa de traducción
	translated_data = {}
	for k, v in data_to_process.items():
		if k in translation_map:
			translated_key = translation_map[k]
			translated_data[translated_key] = v

    # Crear y retornar el DataFrame
	#df = pd.DataFrame([translated_data])
	return translated_data
