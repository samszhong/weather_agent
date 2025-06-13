# Azure AI Weather Agent

This is a Python project for an Azure AI Foundry agent that retrieves weather information using the OpenWeatherMap API.

## Features

- **Instruction to Agent:**  
  You are an AI agent that retrieves weather information using a function call.
- **Action:**  
  The agent calls the OpenWeatherMap API to fetch current weather based on user-provided location using a secure API key.

## Setup

1. Clone the repository and install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenWeatherMap API key as an environment variable.  
   You can copy `.env.example` to `.env` and edit it, or set it directly:
   ```
   export WEATHER_API_KEY=your_openweathermap_api_key_here
   ```

3. Run the agent:
   ```bash
   python main.py
   ```

4. Enter a location (e.g., "London,uk") to get current weather information.

## Example API Call

```
https://api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=your_api_key
```

## Requirements

- Python 3.8+
- `requests`
- `python-dotenv`
- `azure-ai-foundry`

## Security

- The OpenWeatherMap API key is now read from the `WEATHER_API_KEY` environment variable.
- Do not hard-code your API key in the source code or share your `.env` file.

## License

MIT License
