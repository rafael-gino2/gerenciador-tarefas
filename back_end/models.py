from datetime import datetime
from database import tarefas_collection #Tarefas collection é a coleção onde as tarefas vão ser salvas

def status(finalizada, data_meta):
    agora = datetime.now()
    if finalizada == True:
        return "Finalizada"
    elif agora > data_meta:
        return "Atrasada"
    else:
        return "Pendente"


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

nome = input("Digite o nome da tarefa: ")
descricao = input("Digite a descrição da tarefa: ")
data_conclusao_str = input("Digite a data de conclusão da tarefa (DD/MM/AAAA): ")

adicionar_tarefa(nome, descricao, data_conclusao_str)

