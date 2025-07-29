import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code != 200:
            print("Error:", data.get("message", "Something went wrong."))
            return

        city = data['name']
        country = data['sys']['country']
        temp_c = data['main']['temp']
        weather = data['weather'][0]['description']

        print(f"\nWeather in {city}, {country}:")
        print(f"Temperature: {temp_c}°C / {temp_c * 9/5 + 32:.1f}°F")
        print(f"Condition: {weather.title()}")

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    print("--- WeatherCLI ---")
    city = input("Enter city name: ")
    api_key = input("Enter your OpenWeatherMap API key: ")
    get_weather(city, api_key)
