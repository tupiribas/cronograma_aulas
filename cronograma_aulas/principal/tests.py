# principal/tests.py

import os
from django.test import TestCase, Client
from django.urls import reverse
import psycopg2
from .models import Mensagem
import uuid
from dotenv import load_dotenv
load_dotenv()

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

# Teste de conexao

try:
    conn = psycopg2.connect(
        dbname=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        port=os.getenv('DB_PORT')
    )
    print("Conexão ao banco de dados bem-sucedida!")
except Exception as e:
    print(f"Erro ao conectar ao banco de dados: {e}")