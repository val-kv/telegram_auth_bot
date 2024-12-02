from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('telegram-login/', views.telegram_login, name='telegram_login'),
    path('check-auth-status/', views.check_auth_status, name='check_auth_status'),
]
