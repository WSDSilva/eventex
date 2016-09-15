from django.db import models

class Subscription(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=11)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    create_at = models.DateTimeField(auto_now_add=True)
