from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() #para carregar td q tem no dotenv

# Sua URI do MongoDB (aquela que você copiou)
uri = os.getenv("uri_mongo")

# Conectando ao MongoDB
cliente = MongoClient(uri)

# Selecionando o banco
db = cliente.tarefas

# Selecionando a coleção (tipo tabela)
tarefas_collection = db.tarefa

