from datetime import datetime
import json

import requests

from get_cards_json import get_cards_json
from get_card_images import get_card_images

def get_current_api_version():
    url = "https://db.ygoprodeck.com/api/v7/checkDBVer.php"
    headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    response = requests.get(url,headers=headers)
    api_version = json.loads(response.text)
    try:
        with open('api_version.json','r') as f:
            repo_verson = json.loads(f.read())
    except:
        print('Could not open \'api_version.json\' creating new file...')
        with open('api_version.json','w+') as f:
            f.write(json.dumps(api_version,indent=2))
        get_cards_json()
        get_card_images()
        repo_verson = api_version
        
    if api_version[0]['database_version'] == repo_verson[0]['database_version']:
        print('Repo is up to date with the YGOPRODECK API.')
    else:
        print('Repo is not up to date with the YGOPRODECK API. Starting download.')
        with open('api_version.json','w+') as f:
            f.write(json.dumps(api_version,indent=2))
        get_cards_json()
        get_card_images()

    print(repo_verson)

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    current_day = now.day
    with open('timestamp.json','w+') as f:
        f.write(f"{{ \"year\":{current_year},\"month\":{current_month},\"day\":{current_day} }}")


if __name__ == "__main__":
    get_current_api_version()