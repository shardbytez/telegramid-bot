
# GetYourID Bot

A simple Telegram bot that helps you quickly get your Telegram ID and account info. Works in private chats and groups.


 English

Files in repository: bot.py, start.sh, token.txt, venv/

Available commands:

* /id — shows your Telegram ID
* /me — shows your account info (username, first name, ID)
* /help — list of commands and guide links

Usage:

* Directly in private chat with the bot
* Add the bot to a group (it will reply to /id, /me, /help)

How to install and run on server:

1. Clone repository: git clone [git@github.com](mailto:git@github.com)\:shardbytez/telegramid-bot.git && cd telegramid-bot
2. Create venv: python3 -m venv venv && source venv/bin/activate
3. Install deps: pip install -r requirements.txt (or manually pip install pytelegrambotapi)
4. Get token from @BotFather and add it to token.txt
5. Run bot: ./start.sh (auto-restarts if crash)

Guides:

* RU → [https://telegra.ph/Gajd-dlya-GetYourID-Bot-09-13]
* EN → [https://telegra.ph/Guide-for-GetYourID-Bot-09-13-2]

Author: @Coinbix17 https://t.me/Coinbix17


Русский

Простой Telegram-бот, который помогает быстро узнать ваш Telegram ID и информацию об аккаунте. Работает в личных чатах и группах.

Файлы в репозитории: bot.py, start.sh, token.txt, venv/

Доступные команды:

* /id — показывает ваш Telegram ID
* /me — показывает информацию об аккаунте (username, имя, ID)
* /help — список команд и ссылки на гайды

Использование:

* Напрямую в личном чате с ботом
* Добавить бота в группу (он отвечает на /id, /me, /help)

Как установить и запустить на сервере:

1. Клонировать репозиторий: git clone [git@github.com](mailto:git@github.com)\:shardbytez/telegramid-bot.git && cd telegramid-bot
2. Создать виртуальное окружение: python3 -m venv venv && source venv/bin/activate
3. Установить зависимости: pip install -r requirements.txt (или вручную pip install pytelegrambotapi)
4. Получить токен через @BotFather и добавить его в файл token.txt
5. Запустить бота: ./start.sh (автоматически перезапускается при сбое)

Гайды:

* RU → [https://telegra.ph/Gajd-dlya-GetYourID-Bot-09-13]
* EN → [https://telegra.ph/Guide-for-GetYourID-Bot-09-13-2]

Автор: @Coinbix17 https://t.me/Coinbix17
