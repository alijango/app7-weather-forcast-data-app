import requests

API_KEY = "cf573dabb5997768e8ef59feb0920e2a"


def get_data(place, forcast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}" \
          f"&appid={API_KEY}"
    responds = requests.get(url)
    data = responds.json()
    filtered_data = data['list']
    nr_values = 8 * forcast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


if __name__ == "__main__":
    print(get_data('canada', 2))
