from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv() #para carregar td q tem no dotenv

#  URI do MongoDB
uri = os.getenv("uri_mongo")

# Conectando ao MongoDB
cliente = MongoClient(uri)

# Selecionando o banco q iremos usar
db = cliente.tarefas

# Selecionando a coleção (tipo tabela)
tarefas_collection = db.tarefa
users_collection = db.users

