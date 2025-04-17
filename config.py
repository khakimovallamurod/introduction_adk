import os
from dotenv import load_dotenv

load_dotenv()
def get_weather_api():
    api_key = os.getenv("WEATHER_API_KEY")
    if None is api_key:
        return "Not found Api key"
    return api_key

def get_token():
    token = os.getenv("TOKEN")
    if None is token:
        return "Not found token"
    return token