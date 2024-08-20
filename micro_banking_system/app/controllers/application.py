from app.controllers.datarecord import DataRecord
from bottle import redirect, template, request

class Application:

    def __init__(self):
        self.pages = {
            'index': self.index,
            'login': self.login,
            'cadastro': self.cadastro,
            'area_membros': self.area_membros
        }
        self.__model = DataRecord()

    def render(self, page):
        content = self.pages.get(page, self.index)
        return content()

    def index(self):
        self.__model.logout()
        return template('app/views/html/index')

    def area_membros(self):
        email = self.__model.get_user_email()
        return template('app/views/html/area_membros', email=email)

    def cadastro(self):
        if request.method == 'POST':
            first_name = request.forms.get('firstName')
            last_name = request.forms.get('lastName')
            email = request.forms.get('registerEmail')
            password = request.forms.get('registerPassword')
            dob = request.forms.get('registerDob')

            self.__model.book(first_name, last_name, email, password, dob)
            return template('app/views/html/register', success=True, name=first_name)
        else:
            return template('app/views/html/register', success=False)

    def login(self):
        if request.method == 'POST':
            email = request.forms.get('loginEmail')
            password = request.forms.get('loginPassword')

            if self.__model.check_user(email, password):
                return redirect(f'/area_membros')
            else:
                return template('app/views/html/login', error=True)
        return template('app/views/html/login')

    def is_authenticated(self):
        return self.__model.logon()

    def authenticate_user(self, email, password):
        if self.__model.check_user(email, password):
            redirect(f'/area_membros')
        else:
            redirect('/login')
