from app.models.user_account import UserAccount
import json
import uuid

class DataRecord():
    # Banco de dados JSON para o recurso Usuários

    def __init__(self):
        # Inicializa as listas de contas de usuários e usuários autenticados
        self.__user_accounts = []
        self.__authenticated_users = {}
        self.read()  # Carrega os dados do arquivo JSON

    def read(self):
        # Lê os dados dos usuários a partir do arquivo JSON
        try:
            with open("app/controllers/db/user_accounts.json", "r") as arquivo_json:
                user_data = json.load(arquivo_json)  # Carrega os dados do JSON
                self.__user_accounts = [UserAccount(**data) for data in user_data]  # Converte os dados em objetos UserAccount
        except FileNotFoundError:
            # Se o arquivo não for encontrado, cria um usuário Guest
            self.__user_accounts.append(UserAccount('Guest', '000000'))

    def book(self, first_name, last_name, username, password):
        # Cria um novo usuário e o adiciona à lista de contas de usuário
        new_user = UserAccount(first_name, last_name, username, password)
        self.__user_accounts.append(new_user)
        with open("app/controllers/db/user_accounts.json", "w") as arquivo_json:
            user_data = [vars(user_account) for user_account in self.__user_accounts]  # Converte os objetos em dicionários
            json.dump(user_data, arquivo_json)  # Salva os dados atualizados no arquivo JSON

    def getCurrentUser(self, session_id):
        # Retorna o usuário atual com base no ID de sessão
        if session_id in self.__authenticated_users:
            return self.__authenticated_users[session_id]
        return None

    def update_user(self, user):
        # Atualiza os dados de um usuário existente
        for i, existing_user in enumerate(self.__user_accounts):
            if existing_user.username == user.username:
                self.__user_accounts[i] = user  # Substitui o usuário existente pelo atualizado
                break
        with open("app/controllers/db/user_accounts.json", "w") as arquivo_json:
            user_data = [vars(user_account) for user_account in self.__user_accounts]  # Converte os objetos em dicionários
            json.dump(user_data, arquivo_json)  # Salva os dados atualizados no arquivo JSON

    def checkUser(self, username, password):
        # Verifica se o nome de usuário e a senha correspondem a um usuário registrado
        for user in self.__user_accounts:
            if user.username == username and user.password == password:
                session_id = str(uuid.uuid4())  # Gera um novo ID de sessão
                self.__authenticated_users[session_id] = user  # Associa o ID de sessão ao usuário autenticado
                return session_id
        return None

    def logout(self, session_id):
        # Remove o usuário autenticado da lista de usuários autenticados com base no ID de sessão
        if session_id in self.__authenticated_users:
            del self.__authenticated_users[session_id]

    def email_exists(self, email):
        # Verifica se o email (nome de usuário) já está registrado
        return any(user.username == email for user in self.__user_accounts)
