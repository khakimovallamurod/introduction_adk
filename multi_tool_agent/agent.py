import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
# import config
import requests

def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city.

    Args:
        city (str): The name of the city for which to retrieve the weather report.

    Returns:
        dict: status and result or error msg.
    """
    
    url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query={city}"
    response = requests.get(url)
    data = response.json()

    if 'current' not in data:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }
    else:
        temperature = data['current']['temperature']
        weather_desc = data['current']['weather_descriptions'][0]
        country = data['location']['country']
        region = data['location']['region']
        localtime = data['location']['localtime']

        return {
            "status": "success",
            "report": (
                f"Country: {country}\nCity: {region}\nTemperature: {temperature}°C\nWeather: {weather_desc}\nLocal Time: {localtime}"
               
            ),
        }

def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city.

    Args:
        city (str): The name of the city for which to retrieve the current time.

    Returns:
        dict: status and result or error msg.
    """

    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": (
                f"Sorry, I don't have timezone information for {city}."
            ),
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = (
        f'The current time in {city} is {now.strftime("%Y-%m-%d %H:%M:%S %Z%z")}'
    )
    return {"status": "success", "report": report}


root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash-exp",
    description=(
        "Shahardagi vaqt va ob-havo haqida savollarga javob beruvchi agent."
    ),
    instruction=(
        "Assalomu alaykum! Xush kelibsiz! Men sizga shahardagi vaqt va ob-havo haqidagi savollaringizga yordam bera olaman. Marhamat, savolingizni bering."
    ),
    tools=[get_weather, get_current_time],
)