from app.controllers.application import Application
from bottle import Bottle, route, run, request, redirect, template, static_file

app = Bottle()
ctl = Application()

#-----------------------------------------------------------------------------
# Rotas:

# Arquivos estáticos:
@app.route('/static/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./app/static')

# Boas-vindas ao usuário
@app.route('/')  # sempre que acessar home, o logout é automaticamente realizado
@app.route('/user/<unknown>')
def index(unknown=None):
    if not unknown:
        return ctl.render('index')
    else:
        if ctl.is_authenticated():
            return ctl.render('area_membros')
        else:
            redirect('/login')

# Rota para renderizar a página de cadastro `register.html` (GET)
@app.route('/register', method='GET')
def register():
    return template('register')

# Rota para cadastro (POST)
@app.route('/register', method='POST')
def action_register():
    first_name = request.forms.get('firstName')
    last_name = request.forms.get('lastName')
    email = request.forms.get('registerEmail')
    password = request.forms.get('registerPassword')
    dob = request.forms.get('registerDob')
    ctl.__model.book(first_name, last_name, email, password, dob)
    return redirect('/login')  # Redireciona para login após cadastro

# Rota para login (GET)
@app.route('/login', method='GET')
def login():
    return ctl.render('login')

# Rota para login (POST)
@app.route('/login', method='POST')
def action_login():
    email = request.forms.get('loginEmail')
    password = request.forms.get('loginPassword')
    if ctl.authenticate_user(email, password):
        return redirect('/area_membros')
    else:
        return template('login', error=True)

# Rota para área de membros
@app.route('/area_membros')
def area_membros():
    if ctl.is_authenticated():
        return ctl.render('area_membros')
    else:
        return redirect('/login')

#-----------------------------------------------------------------------------

if __name__ == '__main__':
    run(app, host='localhost', port=8080, debug=True)
