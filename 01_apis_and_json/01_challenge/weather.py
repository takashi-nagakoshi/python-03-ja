import requests
from datetime import datetime, timezone

API_KEY = "537db9e92951c846cce94e37286c388c"

def search_city(query):
    url = f"http://api.openweathermap.org/geo/1.0/direct?q={query}&limit=5&appid={API_KEY}"
    response = requests.get(url)
    return response.json()

def weather_forecast(lat, lon):
    url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    daily_forecasts = {}
    for forecast in data['list']:
        timestamp = forecast['dt']
        date = datetime.fromtimestamp(timestamp, tz=timezone.utc).date()
        temp = forecast['main']['temp']
        weather = forecast['weather'][0]['description']
        
        # 各日の12:00の予報を取得
        if date not in daily_forecasts or datetime.fromtimestamp(timestamp, tz=timezone.utc).hour == 12:
            daily_forecasts[date] = {'date': date, 'temp': temp, 'weather': weather}
    
    # 辞書をリストに変換して5日間の予報を返却
    return list(daily_forecasts.values())[:5]

def main():
    while True:
        try:
            query = input("City?\n> ")
            if not query:
                print("Please enter a valid city name.")
                continue

            cities = search_city(query)
            if not cities:
                print("City not found. Please try again.")
                continue

            if len(cities) > 1:
                print("Multiple matches found, which city did you mean?")
                for i, city in enumerate(cities, 1):
                    print(f"{i}. {city['name']}, {city['country']}")
                try:
                    choice = int(input("> "))
                    if 1 <= choice <= len(cities):
                        city = cities[choice - 1]
                    else:
                        print("Invalid choice. Please try again.")
                        continue
                except ValueError:
                    print("Invalid choice. Please try again.")
                    continue
            else:
                city = cities[0]

            print(f"Here's the weather in {city['name']}")
            forecasts = weather_forecast(city['lat'], city['lon'])
            for forecast in forecasts:
                print(f"{forecast['date']}: {forecast['weather']} ({forecast['temp']}°C)")
        # キーCtrl+Cを押したら、プログラムを終了
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break

if __name__ == "__main__":
    main()
