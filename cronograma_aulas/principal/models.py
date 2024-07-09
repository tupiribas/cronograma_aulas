import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Teste mensagem hello world

class Usuario(AbstractUser):
    PERFIL_USUARIO = 'usuario'
    PERFIL_COORDENADOR = 'coordenador'
    PERFIL_MASTER = 'master'

    PERFIS = [
        (PERFIL_USUARIO, 'Usuário'),
        (PERFIL_COORDENADOR, 'Coordenador'),
        (PERFIL_MASTER, 'Master'),
    ]

    perfil = models.CharField(max_length=15, choices=PERFIS, default=PERFIL_USUARIO)
    groups = models.ManyToManyField(Group, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_set')

    def is_coordenador(self):
        return self.perfil == self.PERFIL_COORDENADOR
    
    def is_master(self):
        return self.perfil == self.PERFIL_MASTER

class AccessLog(models.Model):
    ip_address = models.GenericIPAddressField()
    path = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)
    usuario_acesso = models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.SET_NULL)
    usuario_agente = models.CharField(max_length=200, blank=True)
    referer = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.ip_address} accessed {self.path} on {self.timestamp}"

class Mensagem(models.Model):
    id = models.UUIDField(primary_key=True, unique=True,
                          default=uuid.uuid4, editable=False)
    texto = models.CharField(max_length=50)

    def __str__(self):
        return self.texto