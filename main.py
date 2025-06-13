import os
from agent.weather_agent import WeatherAgent

def main():
    agent = WeatherAgent()
    agent.run()

if __name__ == "__main__":
    # Load environment variables from .env if present
    from dotenv import load_dotenv
    load_dotenv()
    main()
