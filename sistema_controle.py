from datetime import datetime

class Tarefa():
    def __init__(self, tarefa_id, nome, descricao, data_meta): #só colocar de parametro o que o usuario podera customizar/inserir
        self.tarefa_id = tarefa_id
        self.nome = nome
        self.descricao = descricao
        self.data_meta = datetime.strptime (data_meta, "%d/%m/%Y")

        # valores definidos automaticamente
        self.data_criacao = datetime.now() #vai pegar a data de que a tarefa for criada (import da biblioteca datetime)
        self.finalizada = False # "Finalizada" está de fora do parametro, pois é uma variavel de inicialmente valor fixo. A tarefa sempre vai começar com False (nn finalizada), ent nn é uma variavel q pode ser diferente pra cada tarefa, igual o nome por exemplo

    @property
    def status(self):
        agora = datetime.now()
        if self.finalizada == True:
            return "Finalizada"
        elif agora > self.data_meta:
            return "Atrasada"
        else:
            return "Pendente"

    def __str__(self):
        return f"Id da tarefa: {self.tarefa_id} \n Nome: {self.nome} \n Descrição: {self.descricao} \n Data de conclusão da tarefa: {self.data_meta} \n Data de criação: {self.data_criacao} \n Status da tarefa: {self.status}"

class Gerenciador_tarefas():
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1 #o id começa com 1 e vai aumentando de 1 a 1 de acordo com a quantidade de tarefas adicionadas

    def adicionar_tarefa(self, nome, descricao, data_meta):
        tarefa_id = self.proximo_id # definindo o id da tarefa de acordo com a variavel proximo_id
        nova_tarefa = Tarefa(tarefa_id, nome, descricao, data_meta)
        self.tarefas.append(nova_tarefa)
        self.proximo_id += 1 #Somando 1 para que a proxima tarefa a ser add tenha um id diferente

gerenciador = Gerenciador_tarefas()

nome = input("Digite o nome da tarefa: ")
descricao = input("Digite a descrição da tarefa: ")
data_meta = input("Digite a data de conclusao da tarefa: ")

gerenciador.adicionar_tarefa(nome, descricao, data_meta)

def printando(tarefas):
  for t in tarefas:
    print(t)

printando(gerenciador.tarefas)