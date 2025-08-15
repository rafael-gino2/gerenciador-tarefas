from pymongo import MongoClient

# Sua URI do MongoDB (aquela que você copiou)
uri = "mongodb+srv://rafaelginoofc:G1hXDQQp4iQRcTvS@tarefaca.dxstsa5.mongodb.net/?retryWrites=true&w=majority&appName=tarefaca"

# Conectando ao MongoDB
cliente = MongoClient(uri)

# Selecionando o banco
db = cliente.tarefas

# Selecionando a coleção (tipo tabela)
tarefas_collection = db.tarefa

