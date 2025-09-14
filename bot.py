import os
import sys
from telegram import Update, User
from telegram.ext import Application, CommandHandler, ContextTypes

# load token from file
try:
    with open("token.txt", "r") as f:
        TOKEN = f.read().strip()
except FileNotFoundError:
    print("ERROR: token.txt not found. Create token.txt with your bot token.")
    sys.exit(1)

if not TOKEN:
    print("ERROR: token.txt is empty.")
    sys.exit(1)


# 🔹 /start — показывает только ID
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user: User = update.effective_user
    text = (
        "╭───────────────╮\n"
        "│  Your ID      │\n"
        "├───────────────┤\n"
        f"🆔 {user.id}\n"
        "╰───────────────╯"
    )
    await update.message.reply_text(text)

# 🔹 /id — тоже только ID
async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user: User = update.effective_user
    text = (
        "╭───────────────╮\n"
        "│  Your ID      │\n"
        "├───────────────┤\n"
        f"🆔 {user.id}\n"
        "╰───────────────╯"
    )
    await update.message.reply_text(text)

# 🔹 /me — полная инфо-карточка
async def me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user: User = update.effective_user
    text = (
        "╭───────────────╮\n"
        "│  Your info    │\n"
        "├───────────────┤\n"
        f"🆔 ID: {user.id}\n"
        f"💬 Username: @{user.username if user.username else '—'}\n"
        f"⭐ Premium: {'✅' if getattr(user, 'is_premium', False) else '❌'}\n"
        f"🤖 Bot: {'✅' if user.is_bot else '❌'}\n"
        "╰───────────────╯"
    )
    await update.message.reply_text(text)

# 🔹 /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.type in ["group", "supergroup"]:
        chat_name = update.effective_chat.title
        text = (
            f"👋 Hello! I'm GetYourID Bot for the chat \"{chat_name}\"!\n\n"
            "Available commands:\n"
            "/id — show only your Telegram ID.\n"
            "/me — show info about your account.\n"
            "/help — list of available commands.\n\n"
            "📌 Guides: [RU](https://telegra.ph/Gajd-dlya-GetYourID-Bot-09-13) | [EN](https://telegra.ph/Guide-for-GetYourID-Bot-09-13-2)"
        )
    else:
        text = (
            "👋 Hello! I'm GetYourID Bot!\n\n"
            "Available commands:\n"
            "/id — show only your Telegram ID.\n"
            "/me — show info about your account.\n"
            "/help — list of available commands.\n\n"
            "📌 Guides: [RU](https://telegra.ph/Gajd-dlya-GetYourID-Bot-09-13) | [EN](https://telegra.ph/Guide-for-GetYourID-Bot-09-13-2)"
        )
    await update.message.reply_text(
    text,
    parse_mode="Markdown",
    disable_web_page_preview=True
)
 
def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("id", get_id))
    application.add_handler(CommandHandler("me", me))
    application.add_handler(CommandHandler("help", help_command))

    print("🤖 Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
