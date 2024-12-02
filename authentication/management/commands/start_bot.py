from django.core.management.base import BaseCommand
from authentication.bot import setup_bot

class Command(BaseCommand):
    help = "Запускает Telegram-бота."

    def handle(self, *args, **kwargs):
        setup_bot()
        self.stdout.write(self.style.SUCCESS("Telegram-бот успешно запущен."))