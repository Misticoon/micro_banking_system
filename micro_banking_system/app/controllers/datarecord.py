from app.models.user_account import UserAccount
import json

class DataRecord:
    """Banco de dados JSON para LOGIN de usuários"""

    def __init__(self):
        self.logout()
        self.read()

    def read(self):
        self.__user_accounts = []  # banco (json)
        try:
            with open("app/controllers/db/user_accounts.json", "r") as arquivo_json:
                user_data = json.load(arquivo_json)
                self.__user_accounts = [UserAccount(**data) for data in user_data]
        except FileNotFoundError:
            self.__user_accounts.append(UserAccount('Guest', '000000'))
        self.print()

    def book(self, first_name, last_name, email, password, dob):
        new_user = UserAccount(first_name, last_name, email, password, dob)
        self.__user_accounts.append(new_user)
        with open("app/controllers/db/user_accounts.json", "w") as arquivo_json:
            user_data = [vars(user_account) for user_account in self.__user_accounts]
            json.dump(user_data, arquivo_json)

    def get_user_email(self):
        return self.__user_account.email if self.__user_account else None

    def check_user(self, email, password):
        print(f"Checando usuário: Email: {email}, Password: {password}")
        for user in self.__user_accounts:
            print(f"user = {user.email}, password= {user.password}")
            if user.email == email and user.password == password:
                print("Check realizado com sucesso!")
                self.__user_account = user
                self.__authenticated = True
                return True
        return False

    def logout(self):
        self.__user_account = None
        self.__authenticated = False
        print('Logout realizado com sucesso!')

    def logon(self):
        return self.__authenticated

    def print(self):
        print("Imprimindo as informações de cada usuário cadastrado:")
        if self.__user_accounts:
            for user in self.__user_accounts:
                user.who_r_u()
        else:
            print("Nenhum usuário encontrado.")
