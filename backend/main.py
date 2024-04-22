from fastapi import FastAPI
import requests

#Manejo de excepciones:
import logging
from fastapi import HTTPException, exceptions
from core.exceptions import ProfileNotFoundError, InvalidProfileError

#from fastapi import FastAPIParam
from core.api import datos_demograficos
from core.api1 import view_profile
from core.api2 import view_posts

app = FastAPI(
    title="API Investigación de Influencers",
    description="Funciones de investigación de perfiles de Influencers: Extracción de datos demograficos sobre los seguidores de un influencer, visualización de datos sobre el perfil y vista de metadatos sobre post realizados por una cuenta. Redes Sociales disponibles: Instagram, Facebook, Twitter, Youtube y TikTok.",
    version="1.0.0",
)

def construir_url_perfil(red_social, username):
    base_urls = {
        'Instagram': 'https://instagram.com/',
        'Facebook': 'https://facebook.com/',
        'Twitter': 'https://twitter.com/',
        'Youtube': 'https://youtube.com/user/', # Asume que estás buscando un usuario, no un canal
        'Tiktok': 'https://tiktok.com/@'
    }
    
    # Verifica que la red social proporcionada esté soportada
    if red_social not in base_urls:
        raise ValueError(f"Red social '{red_social}' no soportada. Por favor, elige entre: {list(base_urls.keys())}")
    
    # Construye la URL
    url = base_urls[red_social] + username
    
    return url

class MiExcepcionPersonalizada(HTTPException):
    status_code = 400
    description = "Ocurrió un error inesperado en la aplicación."
    detail = "Se ha producido un problema interno. Inténtalo de nuevo más tarde."

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()]
)

@app.get("/demographics")
def demographics(red_social: str, username: str):

    perfil = construir_url_perfil(red_social, username)

    try:
        # Extrae el nombre del perfil y la plataforma (opcional)

        return datos_demograficos(perfil=perfil)

    except ProfileNotFoundError:
        # Excepción si no se encuentra el perfil
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    except InvalidProfileError:
        # Excepción si el perfil es inválido
        raise HTTPException(status_code=400, detail="Perfil inválido")

    except Exception as e:
        # Excepción genérica para otros errores
#        logger.exception(f"Error al obtener datos demográficos: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get("/view_profile")
def view_profiles(red_social: str, username: str):

    perfil = construir_url_perfil(red_social, username)
    
    try:

        return view_profile(perfil=perfil)
    
    except ProfileNotFoundError:
        # Excepción si no se encuentra el perfil
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    except InvalidProfileError:
        # Excepción si el perfil es inválido
        raise HTTPException(status_code=400, detail="Perfil inválido")

    except Exception as e:
        # Excepción genérica para otros errores
#        logger.exception(f"Error al obtener datos demográficos: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

@app.get("/view_posts")
def view_post(perfil: str, start_date: str, finish_date: str, keyword: str):
    
    try:

        return view_posts(perfil=perfil)
    
    except ProfileNotFoundError:
        # Excepción si no se encuentra el perfil
        raise HTTPException(status_code=404, detail="Perfil no encontrado")

    except InvalidProfileError:
        # Excepción si el perfil es inválido
        raise HTTPException(status_code=400, detail="Perfil inválido")

    except Exception as e:
        # Excepción genérica para otros errores
#        logger.exception(f"Error al obtener datos demográficos: {e}")
        raise HTTPException(status_code=500, detail="Error interno del servidor")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)