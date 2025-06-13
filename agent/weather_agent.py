import os
import requests
from azure.ai.foundry import Agent, action, Context

class WeatherAgent(Agent):
    """
    An Azure AI Foundry Agent that retrieves weather information using OpenWeatherMap API.
    Instruction: You are an AI agent that retrieves weather information using a function call.
    """

    def __init__(self):
        super().__init__()
        self.api_key = os.getenv("WEATHER_API_KEY")
        if not self.api_key:
            raise ValueError("WEATHER_API_KEY environment variable not set.")
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    @action(name="get_weather", description="Retrieve current weather for a given location.")
    def get_weather(self, context: Context, location: str) -> dict:
        params = {
            "q": location,
            "APPID": self.api_key,
            "units": "metric"
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            return {
                "location": location,
                "temperature": data.get("main", {}).get("temp"),
                "weather": data.get("weather", [{}])[0].get("description"),
                "humidity": data.get("main", {}).get("humidity"),
                "wind_speed": data.get("wind", {}).get("speed")
            }
        else:
            return {"error": f"Failed to retrieve weather info: {response.text}"}

    def run(self):
        print("Welcome to the Azure AI Weather Agent!")
        print("You can ask for weather information by providing a location.")
        while True:
            location = input("Enter a location (or 'exit' to quit): ")
            if location.lower() == "exit":
                print("Goodbye!")
                break
            result = self.get_weather(Context(), location)
            print(result)
