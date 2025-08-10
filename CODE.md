## Projeto: Sistema de Controle de Tarefas com Interface + Banco de Dados

## Ideia do projeto: Criar um site onde o usuário possa cadastrar, editar e concluir tarefas, com salvamento em banco de dados local.

# Informações de codigo:

# *Class Tarefa*: Classe para definir todos os atributos que uma tarefa terá (nome, descrição e etc)
- "data_criacao" e "finalizada" não entram no parametro do def init, pois são variaveis com valores fixos iniciais. Resumidamente são valores que inicialmente não poderam ser customizados pelo usuario.

- "Data_meta" está diferente (com o strptime) pois o datetime converte de string para formato de data (datetime), isso porque, sem essa conversão nn tem como comparar "data_meta" com "agora" pois "data_meta" é string e "agora" é datetime. (tipos de dados diferentes)

- a função "status" é um verificador para entender se a tarefa está pendente, atrasada ou concluida. O verificador sabera que a tarefa está concluida quando "finalizada" estiver como True (O valor mudará para true caso o user valide a tarefa como finalizada). Caso o contrario, a tarefa continuara como pendente, ou atrasada dependendo da comparação com a data de criação da tarefa com o dia e horario atual.

- O @property em status serve basicamente só para transformar a função status em um atributo, e usar a função como uma variavel. Fiz status ficar como um atributo pois é uma informação da tarefa, e não uma ação como adicionar tarefa por exemplo. Basicamente transformei em uma variavel da tarefa como nome ou descrição.

# Para concluir:
- Adicionar horario do dia da conclusão da tarefa
