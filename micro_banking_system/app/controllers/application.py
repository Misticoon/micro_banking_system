from app.controllers.datarecord import DataRecord
from bottle import template, redirect, request, response

class Application():

    def __init__(self):
        self.pages = {
            'index': self.index,
            'register': self.register,
            'home': self.home
        }
        self.__model = DataRecord()

    def render(self, page, username=None):
        content = self.pages.get(page, self.index)
        if username:
            return content(username)
        return content()


    def register(self):
        return template('app/views/html/register')

    def index(self):
        return template('app/views/html/index')

    def home(self, username):
        if self.is_authenticated(username):
            session_id = request.get_cookie('session_id')
            user = self.__model.getCurrentUser(session_id)
            return template('app/views/html/home', transfered=True, current_user=user)
        return template('app/views/html/home', transfered=False)

    def is_authenticated(self, username):
        session_id = request.get_cookie('session_id')
        current_user = self.__model.getCurrentUser(session_id)
        return current_user and username == current_user.username

    def authenticate_user(self, username, password):
        session_id = self.__model.checkUser(username, password)
        if session_id:
            response.set_cookie('session_id', session_id, httponly=True, secure=True, max_age=3600)
            redirect(f'/home/{username}')
        redirect('/index')

    def logout_user(self):
        session_id = request.get_cookie('session_id')
        self.__model.logout(session_id)
        response.delete_cookie('session_id')
        redirect('/index')

    def create_user(self, first_name, last_name, email, password, dob):
        if self.__model.email_exists(email):
            # Se o email já existe, você pode redirecionar para uma página de erro ou mostrar uma mensagem de erro
            redirect('/register?error=email_exists')
        else:
            self.__model.book(first_name, last_name, email, password)
            redirect('/index')

    def email_exists(self, email):
        return self.__model.email_exists(email)

