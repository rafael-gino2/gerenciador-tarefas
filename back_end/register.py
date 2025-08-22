from database import users_collection

def criar_user(nome_user, senha):
    while True:
        try:
            user = {
                "Nome de usuario" : nome_user,
                "Senha": senha
            }
            inserindo_db = users_collection.insert_one(user)
            print("User inserido com o id:", inserindo_db.inserted_id)
            break
        except:
            print("User não cadastrado", KeyError)
            break

nome_user = input("Digite o nome do user: ")
senha = input("Digite a senha do user: ")

criar_user(nome_user, senha)