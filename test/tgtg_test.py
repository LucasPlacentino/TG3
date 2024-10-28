from tgtg import TgtgClient
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import time
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

access_token: str = getenv('ACCESS_TOKEN')
refresh_token: str = getenv("REFRESH_TOKEN")
tgtg_user_id: str = getenv('TGTG_USER_ID')
cookie: str = getenv('COOKIE')
try:
    tgtg_client: TgtgClient = TgtgClient(access_token=access_token,
                                        refresh_token=refresh_token,
                                        user_id=tgtg_user_id,
                                        cookie=cookie)
except Exception as e:
    print(e)
    print("Error creating TgtgClient, aborting...")
    sys.exit(1)
time.sleep(2)
items = tgtg_client.get_items()
telegram_text = f"&#128276; There are new items available on TooGoodToGo:\n"
for product in items:
    print("-----------NEW ITEM-----------")
    print("item")
    print(f"item.item_id {product['item']['item_id']}")
    print(f"item.description {product['item']['description'].replace("\n", "")[:100]+"..." if len(product['item']['description'].replace("\n", ""))>100 else product['item']['description'].replace("\n", "")}") # errors='replace' or errors='ignore'
    print(f"item.price_including_taxes {product['item']['price_including_taxes']}")
    print(f"item.item_price {product['item']['item_price']}")
    print(f"item.cover_picture {product['item']['cover_picture']}")
    print(f"item.logo_picture {product['item']['logo_picture']}")
    print(f"item.name {product['item']['name']}")
    #print(item['item'].keys())

    print("--Item's store--")
    print("store")
    print(f"store.store_id {product['store']['store_id']}")
    print(f"store.store_name {product['store']['store_name']}")
    print(f"store.store_location {product['store']['store_location']}")
    print(f"store.description {product['store']['description'].replace("\n", "")}")
    print(f"store.logo_picture {product['store']['logo_picture']}")
    print(f"store.distance {product['store']['distance']}")
    print(f"store.branch {product['store']['branch']}")
    #print(item['store'].keys())

    print("items_available")
    print(product['items_available'])

    print("item_type")
    print(product['item_type'])


    print(str(product['item']['price_including_taxes']['minor_units'])[:-(product['item']['price_including_taxes']['decimals'])] + "." + str(product['item']['price_including_taxes']['minor_units'])[-(product['item']['price_including_taxes']['decimals']):]+" "+product['item']['price_including_taxes']['code'])

    #print(item.keys())

    if product['items_available'] == 0:
        continue
    __price_minor_units = product['item']['price_including_taxes']['minor_units'] # or ['item']['item_price'] ?
    __price_nb_decimals = product['item']['price_including_taxes']['decimals']
    __price_code = product['item']['price_including_taxes']['code']
    price: str = str(__price_minor_units)[:-(__price_nb_decimals)] + "." + str(__price_minor_units)[-(__price_nb_decimals):]+" "+__price_code
    item_name = product['item']['name']
    item_description = product['item']['description']
    item_id = product['item']['item_id']
    logo_url = product['item']['logo_picture']['current_url'] # same as store.logo_picture
    picture_url = product['item']['cover_picture']['current_url']
    store_name = product['store']['store_name']
    store_id = product['store']['store_id']
    store_location = product['store']['store_location']['address']['address_line']
    store_branch = product['store']['branch']
    item_tag = product['item_type']
    telegram_text += f"- <b>{store_name}</b> ({store_branch}): {product['items_available']} available\n"
    #modified_item_description = item_description.replace("\n", "")[:100]+"..." if len(item_description.replace("\n", ""))>100 else item_description.replace("\n", "")
    modified_item_description = item_description
    telegram_text += f"  {item_name} <code>({price})</code> [{item_tag}]:\n"
    telegram_text += f"   <blockquote expandable><b>Location: {store_location}</b>\n{modified_item_description}</blockquote>\n"

telegram_text += f'<a href="https://tgtg.onelink.me/OGjG"><b>&#10145;Open TGTG App</b></a>\n'
print(telegram_text)
#print(items)

