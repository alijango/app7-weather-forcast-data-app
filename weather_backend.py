import requests
import pandas as pd

API_KEY = "cf573dabb5997768e8ef59feb0920e2a"

def get_data(place, days=None, option=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    responds = requests.get(url)
    data = responds.json()
    return data



if __name__ == "__main__":
    data_w = get_data(place='canada')
    print(data_w['list'][0]['dt_txt'][:10])
    temp = data_w['list'][0]['main']['temp']
    print(type(temp))
    print((temp / 10))