from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from .models import TelegramToken
from django.contrib.auth.models import User

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Обработчик команды /start"""
    token = context.args[0] if context.args else None
    if not token:
        await update.message.reply_text("Ошибка: отсутствует токен для авторизации.")
        return

    try:
        telegram_token = TelegramToken.objects.get(token=token)
    except TelegramToken.DoesNotExist:
        await update.message.reply_text("Ошибка: токен не найден или устарел.")
        return

    # Получаем данные пользователя Telegram
    tg_user = update.message.from_user
    username = tg_user.username or tg_user.first_name

    # Создаем или находим пользователя Django
    user, created = User.objects.get_or_create(username=username)

    # Связываем токен с пользователем
    telegram_token.user = user
    telegram_token.save()

    await update.message.reply_text(f"Привет, {username}! Вы успешно авторизовались.")

def setup_bot():
    """Настройка и запуск Telegram-бота."""
    from django.conf import settings

    TELEGRAM_BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN
    if not TELEGRAM_BOT_TOKEN:
        raise ValueError("Необходимо указать TELEGRAM_BOT_TOKEN.")

    # Создаем приложение Telegram
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Регистрируем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()
