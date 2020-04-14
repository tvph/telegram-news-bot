# Telegram bot to get news
### Functionalities
* This bot will crawl the first page of [vnexpress](https://vnexpress.net) then save the content to data base, then display to user when /news command is typed.
* It uses *polling*: periodically connect's to Telegram's servers to check a new update for your bot [see](https://github.com/python-telegram-bot/python-telegram-bot/wiki/Webhooks#creating-a-self-signed-certificate-using-openssl). Run 3 task crawl-save, clean, handle user's command parallelly
### Requirements:
* [python](https://www.python.org "python") version 3
* [pipenv](https://pipenv.pypa.io/en/latest/ "pipenv") - you can install it by following the documentation
### Main dependencies
* `python 3.8.2`
* `beautifulsoup4`
* `requests`
* `python-telegram-bot`
* `schedule`
* `sqlalchemy`
* `concurrent.futures`
### How to use this bot
1. Use `git` to clone this repo to your local machine
2. Change the current dir to the repo which you cloned
3. Run the command `pipenv install`, then run `pipenv shell` to active the virtual environment
4. On telegram [Bot Father](https://telegram.me/BotFather "Bot Father") you make a new bot, then save the token to `token.json` file follow this format: `"token": "TELEGRAM_BOT_TOKEN_STRING"`
5. Open `Pipfile` add `[scripts] bot = "python run.py token.json"` to the end of this file
6. Then run command `pipenv run bot` to run this bot
