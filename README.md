[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Scratch Telegram Bot
Create a Telegram bot using scratch.mit.edu (proof of concept)

> ### ⚠️ Be careful when using eval block, since you're executing Python code on YOUR MACHINE.

## Requirements
- Python 3.6 or higher
- [Requestly](https://requestly.io) browser extension

----
## How to use
- `$ python -m pip install -r requirements.txt`
- Open [Requestly settings](https://app.requestly.io/rules/)
- Add a _"Replace Host"_ rule
- Replace `https://translate-service.scratch.mit.edu/` with `http://localhost:5000/` and save rule settings
- Replace `api_id`, `api_hash` (you can obtain those on https://my.telegram.org/apps), `bot_token` (Obtain it from [BotFather](https://t.me/BotFather)) parameters in `Client` instance in `main.py`
- `$ python main.py`
- Open https://scratch.mit.edu/projects/504626732 or create your own project uploading `Scratch Telegram Bot.sb3` on Scratch.
- Run the project and send `/start` to your Telegram bot

----
## Credits
Thanks to [ShishCat](https://github.com/ShiSHcat/) for telling me how to MITM Scratch's translator plugin, [Dan](https://github.com/delivrance/) for his amazing library ([Pyrogram](https://github.com/pyrogram/pyrogram/)).
