from telegram import Bot
from tgtg import TgtgClient
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import time
import asyncio
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

telegram_bot_id: str = getenv('TG_BOT_ID')
telegram_chat_id: str = getenv('TG_CHAT_ID')
access_token: str = getenv('ACCESS_TOKEN')
refresh_token: str = getenv("REFRESH_TOKEN")
tgtg_user_id: str = getenv('TGTG_USER_ID')
cookie: str = getenv('COOKIE')

async def main():
    try:
        tgtg_client: TgtgClient = TgtgClient(access_token=access_token,
                                             refresh_token=refresh_token,
                                             user_id=tgtg_user_id,
                                             cookie=cookie)
    except Exception as e:
        print(e)
        print("Error creating TgtgClient, aborting...")
        sys.exit(1)
    await asyncio.sleep(1)
    try:
        bot: Bot = Bot(telegram_bot_id)
    except Exception as e:
        print(e)
        print("Error creating Telegram bot, aborting...")
        sys.exit(1)

    await asyncio.sleep(1)
    all_products = tgtg_client.get_items()

    # emojis: https://www.quackit.com/character_sets/emoji/emoji_v3.0/unicode_emoji_v3.0_characters_all.cfm
    telegram_text = f"<i><b>[TEST]</b></i>&#128276; <u>Some of your favorite items available on TooGoodToGo:</u>\n"
    
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

    await asyncio.sleep(1)
    print("Sending message...")
    response = await bot.send_message(chat_id=telegram_chat_id,
                                text=telegram_text,
                                #disable_web_page_preview=True,
                                parse_mode="HTML") # MarkdownV2 or HMTL
    print("Message sent.")
    print("response: ",end="")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())