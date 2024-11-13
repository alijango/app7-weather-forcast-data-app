import requests
import pandas as pd

API_KEY = "cf573dabb5997768e8ef59feb0920e2a"

def get_data(place, forcast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    responds = requests.get(url)
    data = responds.json()
    filtered_data = data['list']
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    if kind == 'Temperature':
        filtered_data = [dic['main']['temp'] for dic in filtered_data]
    if kind == 'Sky':
        filtered_data = [dic['weather'][0]['main'] for dic in filtered_data]
    return filtered_data



if __name__ == "__main__":
    print(get_data('canada', 2, 'Sky'))
