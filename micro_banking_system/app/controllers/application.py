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

    def home(self, bank_account_id):
        if self.is_authenticated(bank_account_id):
            session_id = request.get_cookie('session_id')
            user = self.__model.getCurrentUser(session_id)
            return template('app/views/html/home', transfered=True, current_user=user)
        return template('app/views/html/home', transfered=False)

    def is_authenticated(self, bank_account_id):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)
        return current_user and bank_account_id == current_user.bank_account_id

    def authenticate_user(self, username, password):
        session_id = self.__model.checkUser(username, password)
        if session_id:
            user = self.__model.getCurrentUser(session_id)
            response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
            redirect(f'/home/{user.bank_account_id}')
        redirect('/')

    def logout_user(self):
        session_id = request.get_cookie('session_id')
        self.__model.logout(session_id)
        response.delete_cookie('session_id')
        redirect('/index')

    def create_user(self, first_name, last_name, email, password, dob):
        if self.__model.email_exists(email):
            redirect('/register?error=email_exists')
        else:
            self.__model.book(first_name, last_name, email, password)
            redirect('/')

    def email_exists(self, email):
        return self.__model.email_exists(email)
