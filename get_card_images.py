import json
import ssl
import time
from pathlib import Path
from urllib.request import urlretrieve

from tqdm import tqdm

def get_card_images(overwrite=False):
    print('Starting up.')

    ssl._create_default_https_context = ssl._create_unverified_context

    with open('card_info/current/json/ygo_cards.json','r') as f:
        card_json = json.loads(f.read())

    
    #headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"}

    for i in tqdm(card_json['data']):
        card_id = i['id']

        # Flags to indicate if the image(s) have been downloaded or not.
        #   False = Not downloaded in this repo.
        #   True = Downloaded and exists in this repo.
        has_normal_image = Path(f'card_images/image_normal/{card_id}.jpg').is_file()
        has_small_image = Path(f'card_images/image_small/{card_id}.jpg').is_file()
        has_cropped_image = Path(f'card_images/image_cropped/{card_id}.jpg').is_file()
        
        try:
            card_normal_image_url = i['card_images'][0]['image_url']
        except:
            print(f'\nCould not find a normal-sized image of card ID #{card_id}.')
            card_normal_image_url = None
        
        try:
            card_small_image_url = i['card_images'][0]['image_url_small']
        except:
            print(f'\nCould not find a small-sized image of card ID #{card_id}.')
            card_small_image_url = None

        try:
            card_cropped_image_url = i['card_images'][0]['image_url_cropped']
        except:
            print(f'\nCould not find a cropped image of card ID #{card_id}.')
            card_cropped_image_url = None


        if (overwrite == True or has_normal_image == False) and card_normal_image_url != None:
            print(f'\nDownloading the normal-sized image for card ID #{card_id}.')
            try:
                urlretrieve(card_normal_image_url,filename=f'card_images/image_normal/{card_id}.jpg')
            except:
                print('The card could not be downloaded at this time.')
                time.sleep(4)
            time.sleep(0.25)

        if (overwrite == True or has_small_image == False) and card_small_image_url != None:
            print(f'\nDownloading the small-sized image for card ID #{card_id}.')
            try:
                urlretrieve(card_small_image_url,filename=f'card_images/image_small/{card_id}.jpg')
            except:
                print('The card could not be downloaded at this time.')
                time.sleep(4)
                
            time.sleep(0.25)

        if (overwrite == True or has_cropped_image == False) and card_cropped_image_url != None:
            print(f'\nDownloading the cropped image for card ID #{card_id}.')
            try:
                urlretrieve(card_cropped_image_url,filename=f'card_images/image_cropped/{card_id}.jpg')
            except:
                print('The card could not be downloaded at this time.')
                time.sleep(4)
            time.sleep(0.25)


if __name__ == "__main__":
    get_card_images(True)