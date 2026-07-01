import urllib.request

def fetch_weather(city):
    url = f"https://api.weather.com/v1/{city}"
    response = urllib.request.urlopen(url)
    return response.read()
