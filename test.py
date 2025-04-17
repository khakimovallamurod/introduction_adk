import requests

API_KEY = 'cef1e2ddeb496ce867b641d1e97e339e'

def get_weather(city):
    try:
        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
        response = requests.get(url)
        data = response.json()

        if 'current' not in data:
            return f"Error: {data.get('error', {}).get('info', 'Unknown error')}"

        temperature = data['current']['temperature']
        weather_desc = data['current']['weather_descriptions'][0]
        country = data['location']['country']
        region = data['location']['region']
        localtime = data['location']['localtime']

        return f"Country: {country}\nCity: {region}\nTemperature: {temperature}°C\nWeather: {weather_desc}\nLocal Time: {localtime}"
    
    except Exception as ex:
        return f"Error: {str(ex)}"

print(get_weather("salom"))
