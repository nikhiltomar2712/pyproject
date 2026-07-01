import urllib.request

def fetch_weather(city):
    url = f"https://api.weather.com/v1/{city}"
    try:
        response = urllib.request.urlopen(url)
        return response.read()
    except Exception as e:
        print(f"Error fetching weather: {e}")
        # Missing return statement causes NoneType error in callers
