from datetime import datetime
from database import tarefas_collection #Tarefas collection é a coleção onde as tarefas vão ser salvas
from flask import Flask
from bson import ObjectId # O id sozinho é só string, ent precisamos do ObjectId do MongoDB para identificar o Id como id de fato, já que o id só seria varios numeros ou caracteres aleatorios sem o ObjectId

app = Flask(__name__)

def status(finalizada, data_meta):
    agora = datetime.now()
    if finalizada == True:
        return "Finalizada"
    elif agora > data_meta:
        return "Atrasada"
    else:
        return "Pendente"

@app.route("/tarefas", methods=["POST"])
def adicionar_tarefa(nome, descricao, data_conclusao_str):
    while True:
        try:
            data_conclusao_str = datetime.strptime(data_conclusao_str, "%d/%m/%Y") #serve para converter a string em formato datetime
            tarefa={ #criando um dict para criar a tarefa
                "Nome": nome,
                "Descrição": descricao,
                "Data de Criação": datetime.now(),
                "Data de conclusão": data_conclusao_str,
                "Finalizada": False, # A tarefa inicia com False, pois ela começa como pendente.
            }
            inserindo_db = tarefas_collection.insert_one(tarefa) #usa o metodo insert_one do mongodb para inserir a tarefa na coleção
            print("Tarefa inserida com id:", inserindo_db.inserted_id)
            break
        except ValueError:
            print("Data invalida.")

@app.route("/tarefas", methods=["GET"])
def listar_tarefa():
    tarefas = list(tarefas_collection.find()) # o find vai encontrar/listar todas as tarefas do nosso collection
    for i in tarefas:
        print(i)

@app.route("/tarefas/<id>", methods=["DELETE"])
def deletar_tarefa(id):
    deletar = tarefas_collection.delete_one({"_id": ObjectId(id)}) # o id fica nas chaves pois estamos decidindo oq vamos deleter do banco por meio de chave e valor(dicionario), nesse caso deletara o item que tiver a chave _id e o valor objectId com o id
    if deletar.deleted_count == 1: # se o deletar_one achar algum item do banco com o id selecionado printa como tarefa apagada
        print("Tarefa apagada")
    else:
        print("Erro ao apagar tarefa")

nome = input("Digite o nome da tarefa: ")
descricao = input("Digite a descrição da tarefa: ")
data_conclusao_str = input("Digite a data de conclusão da tarefa (DD/MM/AAAA): ")

adicionar_tarefa(nome, descricao, data_conclusao_str)

