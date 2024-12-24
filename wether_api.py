import requests

API_KEY = "9401c18a5b13ebd028f7daec4c84b68e"  # Вставьте свой API-ключ
CITY = "Kyiv"               # Замените на свой город

def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        description = data['weather'][0]['description'].capitalize()
        return f"Temperature: {temperature}°C, {description}"
    
    else:
        return "Weather error"
