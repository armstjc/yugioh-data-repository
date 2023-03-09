import json
from datetime import datetime

import requests


def get_cards_json():
    print('Starting up.')
    url = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day

    if current_month < 10:
        current_month = f"0{current_month}"

    if current_day < 10:
        current_day = f"0{current_day}"

    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    response = requests.get(url,headers=headers)
    json_data = json.loads(response.text)

    with open(f'card_info/current/json/ygo_cards.json','w+') as f:
        f.write(json.dumps(json_data,indent=2))

    with open(f'card_info/historical/json/{current_year}_{current_month}_{current_day}.json','w+') as f:
        f.write(json.dumps(json_data,indent=2))

if __name__ == "__main__":
    get_cards_json()