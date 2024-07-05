import uuid
from django.db import models

class Mensagem(models.Model):
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    texto = models.CharField(max_length=50)

    def __str__(self):
        return self.texto