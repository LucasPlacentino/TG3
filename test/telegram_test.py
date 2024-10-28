from telegram import Bot
from os import getenv
from dotenv import load_dotenv
load_dotenv()
import time
import asyncio
import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

async def main():
    telegram_bot_id: str = getenv('TG_BOT_ID')
    telegram_chat_id: str = getenv('TG_CHAT_ID')

    bot: Bot = Bot(telegram_bot_id)
    # emojis: https://www.quackit.com/character_sets/emoji/emoji_v3.0/unicode_emoji_v3.0_characters_all.cfm
    telegram_text = f"<i><b>[TEST]</b></i>&#128276; <u>Some of your favorite items available on TooGoodToGo:</u>\n"
    telegram_text += f"- <b>store_name</b> (branch): X available\n"
    modified_item_description = "Quite a long description, so it will be cut off and replaced with an expandable blockquote, so you can read the full description.\nThis is really really long, lorem ipsum dolor sit amet.\nYepppp"
    telegram_text += f"  item_name (<code>3.99 EUR</code>) [item_tag]:"
    telegram_text += f"   <blockquote expandable><b>Location: address</b>\n{modified_item_description}</blockquote>\n"
    telegram_text += f'<a href="https://tgtg.onelink.me/OGjG"><b>&#10145;<u>Open TGTG App</u></b></a>\n'
    time.sleep(2)
    print("Sending message...")
    response = await bot.send_message(chat_id=telegram_chat_id,
                                text=telegram_text,
                                #disable_web_page_preview=True,
                                parse_mode="HTML") # MarkdownV2 or HMTL
    print("response: ",end="")
    print(response)

if __name__ == "__main__":
    asyncio.run(main())
