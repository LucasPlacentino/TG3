# TG³ _[ 🚧 WIP 🚧 ]_
A fork of [LauPaSat-pl/TGTG notifications](https://github.com/LauPaSat-pl/TGTG_notifications), and inspired by [Der-Henning/tgtg](https://github.com/Der-Henning/tgtg) and [kacpi2442/am_bot](https://github.com/kacpi2442/am_bot/tree/main)

[![tgtg notifications](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications.yml/badge.svg)](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications.yml)
[![tgtg notifications](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications2.yml/badge.svg)](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications2.yml)
[![tgtg notifications](../../actions/workflows/notitications3.yml/badge.svg)](../../actions/workflows/notitications3.yml)

## There are 2 versions: 

||1. Github Actions |2. Self-hosted |
|:---|:---:|:---:|
|**Status**|🟩 Almost fully working|🟨 WIP|
|**Runs on**|Github servers|_Your_ server|
|**_- Features:_**|----------|----------|
|Easy setup|✅|🟨[^1]|
|Notifies available items|✅|✅|
|Shows price of items|✅|✅|
|Shows quantity available|✅|✅|
|Shows store location|✅|✅|
|Shows description|✅|✅|
|Link to open app|✅|✅|
|Prevents repetition[^2]|❌|✅|
|...[^3]|❌|✅|

[^1]: _Not difficult if you know how to run a simple linux server._
[^2]: _Prevents sending notifications for available items that were already sent._
[^3]: TODO._

## Setup:
1. Create a new Telegram bot using BotFather [tutorial](https://core.telegram.org/bots#how-do-i-create-a-bot),  
2. Check your Telegram ID [tutorial](https://www.alphr.com/telegram-find-user-id/),  
3. Install the `tgtg` Python library  
```
pip install tgtg
```
4. Run with `python`  
```python
from tgtg import TgtgClient

client = TgtgClient(email="your_email@example.org")
credentials = client.get_credentials()
```
You should receive an **email** from TooGoodToGo. The client will wait until you validate the login by **clicking the link inside the email**.  

Once you clicked the link, you will get **credentials** and be able to see them with:  
```python
print(credentials)
```

They will look like this:  
```python
{
    'access_token': '<your_access_token>',
    'refresh_token': '<your_refresh_token>',
    'user_id': '<your_user_id>',
    'cookie': '<cookie>',
}
```

## 1. Github Actions workflows
**This runs 100% automatically on Github Actions** (not counting the set up), to check for your favourite available TooGoodToGo items and send you a Telegram message about it. You can make it run periodically, for example every 15 minutes.

### Steps:
1. Fork this repo,  
2. **In your repo** add **secrets** ([tutorial](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)) you got from earlier steps (TooGoodToGo and Telegram), you can check how to name them in `notitications.yml` file,  
    **[DO NOT PUT THEM VISIBLE IN `.py` or `.yml` FILES DIRECTLY OR ELSE YOU WILL HAVE TO REVOKE YOUR CREDENTIALS AND DELETE YOUR FORK]**  
3. Make sure it's up and running.  

## 2. Self-hosted app

TODO  

### Steps:

TODO  
clone  
.env.template -> .env  
docker?  
...  
