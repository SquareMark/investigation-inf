import requests

url = "https://instagram-statistics-api.p.rapidapi.com/community"

querystring = {"url": "https://www.instagram.com/mr.temaz0s/"}

headers = {
    "X-RapidAPI-Key": "f104323bd2mshf25ae6828cdd5c3p17ce63jsn441e4323d851",
    "X-RapidAPI-Host": "instagram-statistics-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

json_data = response.json()

print(json_data)