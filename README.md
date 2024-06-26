# TG³ _[ 🚧 WIP 🚧 ]_
A fork of [LauPaSat-pl/TGTG notifications](https://github.com/LauPaSat-pl/TGTG_notifications), and inspired by [Der-Henning/tgtg](https://github.com/Der-Henning/tgtg) and [kacpi2442/am_bot](https://github.com/kacpi2442/am_bot/tree/main)

[![tgtg notifications](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications.yml/badge.svg)](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications.yml)
[![tgtg notifications](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications2.yml/badge.svg)](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications2.yml)
[![tgtg notifications](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications3.yml/badge.svg)](https://github.com/LucasPlacentino/TG3/actions/workflows/notitications3.yml)

**This runs 100% automatically on Github actions** (not counting the set up), to check for your favourite TooGoodToGo bags and send you a Telegram message about it.

## How to use
1. Create a new Telegram bot using BotFather [tutorial](https://core.telegram.org/bots#how-do-i-create-a-bot),
2. Check your Telegram ID [tutorial](https://www.alphr.com/telegram-find-user-id/),
3. Install the `tgtg` Python library 
```
pip install tgtg
```
4. Run 
``` python
from tgtg import TgtgClient

client = TgtgClient(email="<your_email>")
credentials = client.get_credentials()
```
You should receive an email from TooGoodToGo. The client will wait until you validate the login by clicking the link inside the email.

Once you clicked the link, you will get credentials and be able to use them
``` python
print(credentials)
{
    'access_token': '<your_access_token>',
    'refresh_token': '<your_refresh_token>',
    'user_id': '<your_user_id>',
    'cookie': '<cookie>',
}
```
5. Fork this repo,
6. **In your repo** add secrets ([tutorial](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions#creating-secrets-for-a-repository)) you got from earlier steps (TooGoodToGo and Telegram), you can check how to name them in `notitications.yml` file,
7. Make sure it's up and running. (It's ok, if at least one of the TG³ notifications badges at the top is green)
