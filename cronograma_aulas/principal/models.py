import uuid
from django.db import models

# Teste mensagem hello world


class Mensagem(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    texto = models.CharField(max_length=50)

    def __str__(self):
        return self.texto


class AccessLog(models.Model):
    ip_address = models.GenericIPAddressField()
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} accessed {self.path} on {self.timestamp}"
