from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
from .models import TelegramToken


def login_view(request):
    return render(request, 'login.html')


def telegram_login(request):
    # Генерация уникального токена
    token = get_random_string(32)
    TelegramToken.objects.create(token=token)

    # Ссылка на бота с токеном
    bot_username = "auth_angry_bot"
    bot_link = f"https://t.me/{bot_username}?start={token}"
    return redirect(bot_link)


def check_auth_status(request):
    return JsonResponse({'is_authenticated': request.user.is_authenticated})
