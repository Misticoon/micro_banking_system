from app.controllers.datarecord import DataRecord
from bottle import template, redirect, request, response

class Application():

    def __init__(self):
        self.pages = {
        'index': self.index,
        'register': self.register,
        'home': self.home,
        'deposit': self.deposit,
        'withdraw': self.withdraw,
        'transfer': self.transfer
        }
        self.__model = DataRecord()

    def render(self, page, identifier=None):
        content = self.pages.get(page, self.index)
        if identifier:
            return content(identifier)
        return content()

    def register(self):
        return template('app/views/html/register')

    def index(self):
        return template('app/views/html/index')
    
    def deposit(self):
        return template('app/views/html/deposito')

    def withdraw(self):
        return template('app/views/html/saque')

    def transfer(self):
        return template('app/views/html/transferencia')

    def home(self):
        session_id = request.get_cookie('session_id')
        user = self.__model.getCurrentUser(session_id)
        if not user:
            redirect('/')
        return template('app/views/html/home', transfered=True, current_user=user)

    def deposit(self):
        session_id = request.get_cookie('session_id')
        user = self.__model.getCurrentUser(session_id)
        if not user:
            redirect('/')
        return template('app/views/html/deposito', bank_account_id=user.bank_account_id)

    def withdraw(self):
        session_id = request.get_cookie('session_id')
        user = self.__model.getCurrentUser(session_id)
        if not user:
            redirect('/')
        return template('app/views/html/saque', bank_account_id=user.bank_account_id)

    def transfer(self):
        session_id = request.get_cookie('session_id')
        user = self.__model.getCurrentUser(session_id)
        if not user:
            redirect('/')
        return template('app/views/html/transferencia', bank_account_id=user.bank_account_id)

    def get_current_user(self, session_id):
        return self.__model.getCurrentUser(session_id)

    def update_user(self, user):
        self.__model.update_user(user)  # Implemente a atualização no `DataRecord`

    def is_authenticated(self, bank_account_id):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)
        return current_user and bank_account_id == current_user.bank_account_id

    def authenticate_user(self, username, password):
        session_id = self.__model.checkUser(username, password)
        if session_id:
            response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
            redirect('/home')
        else:
            response.set_cookie('login_error', '1', max_age=10)
            redirect('/')


    def logout_user(self):
        session_id = request.get_cookie('session_id')
        self.__model.logout(session_id)
        response.delete_cookie('session_id')
        redirect('/')

    def create_user(self, first_name, last_name, email, password, dob):
        if self.__model.email_exists(email):
            redirect('/register?error=email_exists')
        else:
            # Cria o usuário
            self.__model.book(first_name, last_name, email, password)
            
            # Autentica o usuário imediatamente
            session_id = self.__model.checkUser(email, password)
            response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
            
            # Redireciona para a página home do usuário logado com parâmetro registered=true
            redirect('/home?registered=true')


    def email_exists(self, email):
        return self.__model.email_exists(email)

    def format_balance(self, balance):
        if balance.is_integer():
            return int(balance)
        return round(balance, 2)

    def process_deposit(self):
        session_id = request.get_cookie('session_id')
        user = self.get_current_user(session_id)
        
        if not user:
            return {'success': False, 'message': 'Usuário não autenticado'}
        
        deposit_data = request.json
        deposit_amount = deposit_data.get('amount')
        
        if deposit_amount and deposit_amount > 0:
            user.balance += deposit_amount
            user.balance = self.format_balance(user.balance)
            self.update_user(user)
            return {'success': True, 'new_balance': user.balance}
        else:
            return {'success': False, 'message': 'Valor inválido para depósito'}

    def process_transfer(self):
        session_id = request.get_cookie('session_id')
        print(f"Session ID: {session_id}")  # Log para depuração
        user = self.get_current_user(session_id)
        
        if not user:
            print("Usuário não autenticado")  # Log para depuração
            return {'success': False, 'message': 'Usuário não autenticado'}
        
        transfer_data = request.json
        destination_account_id = transfer_data.get('destinationAccount')
        amount = transfer_data.get('amount')

        print(f"Transfer data: {transfer_data}")  # Log para depuração

        if amount <= 0:
            return {'success': False, 'message': 'Valor inválido para transferência'}

        if user.balance < amount:
            print("Saldo insuficiente")  # Log para depuração
            return {'success': False, 'message': 'Saldo insuficiente'}

        if user.bank_account_id == destination_account_id:
            return {'success': False, 'message': 'Não é possível transferir para a própria conta'}

        destination_user = next((u for u in self.__model._DataRecord__user_accounts if u.bank_account_id == destination_account_id), None)

        if not destination_user:
            return {'success': False, 'message': 'Conta de destino não encontrada'}

        user.balance -= amount
        destination_user.balance += amount

        user.balance = self.format_balance(user.balance)  # Formatar o saldo
        destination_user.balance = self.format_balance(destination_user.balance)

        self.update_user(user)
        self.update_user(destination_user)

        return {'success': True}

    def process_withdraw(self):
        session_id = request.get_cookie('session_id')
        user = self.get_current_user(session_id)
        
        if not user:
            return {'success': False, 'message': 'Usuário não autenticado'}

        withdraw_data = request.json
        withdraw_amount = withdraw_data.get('amount')

        if withdraw_amount and withdraw_amount > 0:
            if user.balance >= withdraw_amount:
                user.balance -= withdraw_amount
                user.balance = self.format_balance(user.balance)
                self.update_user(user)
                return {'success': True}
            else:
                return {'success': False, 'message': 'Saldo insuficiente'}
        else:
            return {'success': False, 'message': 'Valor inválido para saque'}
