# Github Actions main script

import asyncio
import os
import time
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

from telegram import Bot
from tgtg import TgtgClient


async def main() -> None:
    # get environment variables (from Github repo secrets)
    access_token: str = os.environ['ACCESS_TOKEN']
    refresh_token: str = os.environ["REFRESH_TOKEN"]
    tgtg_user_id: str = os.environ['TGTG_USER_ID']
    cookie: str = os.environ['COOKIE']
    telegram_bot_id: str = os.environ['TG_BOT_ID']
    telegram_chat_id: str = os.environ['TG_CHAT_ID']

    try:
        tgtg_client: TgtgClient = TgtgClient(access_token=access_token,
                                             refresh_token=refresh_token,
                                             user_id=tgtg_user_id,
                                             cookie=cookie)
    except Exception as e:
        print(e)
        print("Error creating TgtgClient, aborting...")
        return
    time.sleep(1)
    bot: Bot = Bot(telegram_bot_id)
    all_products = tgtg_client.get_items()
    #all_items = tgtg_client.get_items(favorites_only=False,
    #                                   latitude=location-lat,
    #                                   longitude=location-long,
    #                                   radius=location-range,
    #                                   page_size=300)
    print(all_products)
    # use Markdown -> end line with two spaces to create new line
    if all(product['items_available'] == 0 for product in all_products):
        return
    telegram_text = f"&#128276; There are new items available on TooGoodToGo:\n"
    for product in all_products:
        amount_available = product['items_available']
        if amount_available > 0:
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

            telegram_text += f"- <b>{store_name}</b> ({store_branch}): {amount_available} available\n"
            #modified_item_description = item_description.replace("\n", "")[:100]+"..." if len(item_description.replace("\n", ""))>100 else item_description.replace("\n", "")
            modified_item_description = item_description
            telegram_text += f"  {item_name} <code>{price}</code> [{item_tag}]:\n"
            telegram_text += f"   <blockquote expandable><b>Location: {store_location}</b>\n{modified_item_description}</blockquote>\n"
        else:
            continue
    telegram_text += f'<a href="https://tgtg.onelink.me/OGjG"><b>&#10145;Open TGTG App</b></a>\n'
    #telegram_text += f"\n**[Open TooGoodToGo](toogoodtogoapp://)**" # doesn't work :(

    
    print("Sending message...")
    response = await bot.send_message(chat_id=telegram_chat_id,
                                      text=telegram_text,
                                      #disable_web_page_preview=True,
                                      parse_mode="HTML") # MarkdownV2 or HMTL
    print(response)
    #for item in await tgtg_client.get_items():
    #
    #    #time.sleep(60)
    #    items_available: int = item['items_available']
    #    if items_available > 0:
    #        telegram_text = f"""## There are {items_available} bags available:
    #        """
    #        await bot.send_message(chat_id=telegram_chat_id,
    #                               text=telegram_text,
    #                               parse_mode=MARKDOWN_V2)


if __name__ == '__main__':
    asyncio.run(main())
    #main()
