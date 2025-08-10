from models import Gerenciador_tarefas

gerenciador = Gerenciador_tarefas()

nome = input("Digite o nome da tarefa: ")
descricao = input("Digite a descrição da tarefa: ")
data_meta = input("Digite a data de conclusao da tarefa: ")

gerenciador.adicionar_tarefa(nome, descricao, data_meta)

def printando(tarefas):
  for t in tarefas:
    print(t)

printando(gerenciador.tarefas)