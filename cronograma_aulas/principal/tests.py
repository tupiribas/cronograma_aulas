# principal/tests.py

from django.test import TestCase, Client
from django.urls import reverse
from .models import Mensagem
import uuid

class MensagemModelTest(TestCase):

    def setUp(self):
        # Mokando o teste
        self.mensagem = Mensagem.objects.create(texto="Mensagem de texto teste")

    def teste_criar_mensagem(self):
        self.assertTrue(isinstance(self.mensagem, Mensagem))
        self.assertEqual(self.mensagem.__str__(), self.mensagem.texto)
        self.assertTrue(isinstance(self.mensagem.id, uuid.UUID))
        print("Teste __str__:", self.mensagem.__str__())


class HelloWorldViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.mensagem = Mensagem.objects.create(texto="Olá Mundo!")
        self.url = reverse('hello_world', args=[self.mensagem.id])

    def teste_hello_world_view(self):
        resposta_http = self.client.get(self.url)
        self.assertEqual(resposta_http.status_code, 200)
        self.assertContains(resposta_http, "Olá Mundo!")
