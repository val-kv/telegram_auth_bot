from django.db import models

class TelegramToken(models.Model):
    token = models.CharField(max_length=64, unique=True)
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
