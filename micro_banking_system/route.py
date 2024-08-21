from app.controllers.application import Application
from bottle import Bottle, route, run, request, static_file
from bottle import redirect, template

app = Bottle()
ctl = Application()

# Rota para servir arquivos estáticos
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

# Rota para a página inicial
@app.route('/')
@app.route('/user/<unknown>')
def index(unknown=None):
    if not unknown:
        return ctl.render('index')
    else:
        if ctl.is_authenticated(unknown):
            return ctl.render('home', unknown)
        else:
            redirect('/index')

# Rota para o registro (GET)
@app.route('/register', method='GET')
def register():
    return ctl.render('register')

# route.py

@app.route('/register', method='POST')
def action_register():
    first_name = request.forms.get('firstName')
    last_name = request.forms.get('lastName')
    email = request.forms.get('registerEmail')
    password = request.forms.get('registerPassword')
    dob = request.forms.get('registerDob')  # Inclua dob na chamada

    # Chama a função para criar um novo usuário
    ctl.create_user(first_name, last_name, email, password, dob)

    # Redireciona para a página inicial após o registro
    redirect('/')



# Outras rotas do aplicativo

@app.route('/home/<username>', method='GET')
def action_home(username=None):
    return ctl.render('home', username)

@app.route('/index', method='GET')
def login():
    return ctl.render('index')

@app.route('/index', method='POST')
def action_index():
    username = request.forms.get('username')
    password = request.forms.get('password')
    ctl.authenticate_user(username, password)

@app.route('/logout', method='POST')
def logout():
    ctl.logout_user()

if __name__ == '__main__':
    run(app, host='localhost', port=8060, debug=True)
