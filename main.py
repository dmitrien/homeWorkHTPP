import time
from datetime import datetime, timedelta, date
from pprint import pprint

import requests as requests

from yandex_disck import YaUploader
# Задание1-------------------------------------------------------------------------------------------------------------

def get_info_request():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    if response.status_code != 200:
        print("Expect error")
    data_hero = response.json()
    return data_hero

def max_intelligence_hero(name_heros):
    heros = []
    for name in get_info_request():
       if name.get('name') in name_heros:
           heros.append(name)

    max_intelligence = {}

    for dict_name in heros:
        max_intelligence[dict_name.get("powerstats").get("intelligence")] = dict_name.get('name')

    return print(max_intelligence.get(max(max_intelligence, key=max_intelligence.get)))

max_intelligence_hero(['Hulk', 'Captain America', 'Thanos'])

# Задание2-------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    path_to_file = ' '
    token = " "
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

# Задание3-------------------------------------------------------------------------------------------------------------

def get_info_request():
    from_date = datetime.now() - timedelta(days=1)
    to_date = datetime.now() + timedelta(days=1)
    url = f'https://api.stackexchange.com/2.3/questions?fromdate={int(time.mktime(from_date.timetuple()))}&todate={int(time.mktime(to_date.timetuple()))}&site=stackoverflow'
    response = requests.get(url)
    if response.status_code != 200:
        print("Expect error")
    data = response.json()
    new_list = data["items"]
    for quest in new_list:
        if 'python' in quest["tags"]:
            pprint(quest)

get_info_request()