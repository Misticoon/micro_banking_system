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
    dob = request.forms.get('registerDob')

    # Verificação do e-mail no servidor usando o novo método público
    if ctl.email_exists(email):
        redirect('/register?error=email_exists')
    else:
        ctl.create_user(first_name, last_name, email, password, dob)
        redirect('/')

@app.route('/email_exists', method='GET')
def email_exists():
    email = request.query.get('email')
    exists = ctl.email_exists(email)
    return {'exists': exists}


# Outras rotas do aplicativo

@app.route('/home', method='GET')
def action_home():
    return ctl.render('home')

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

# Rota para a página de depósito
@app.route('/deposito', method='GET')
def deposito():
    return ctl.render('deposit')

@app.route('/deposito', method='POST')
def process_deposit():
    session_id = request.get_cookie('session_id')
    user = ctl.get_current_user(session_id)
    
    if not user:
        return {'success': False, 'message': 'Usuário não autenticado'}

    deposit_data = request.json
    deposit_amount = deposit_data.get('amount')

    if deposit_amount and deposit_amount > 0:
        user.balance += deposit_amount  # Supondo que o objeto `UserAccount` tenha um atributo `balance`
        ctl.update_user(user)  # Supondo que haja um método para atualizar o usuário no banco de dados
        return {'success': True}
    else:
        return {'success': False, 'message': 'Valor inválido para depósito'}


# Rota para a página de saque
@app.route('/saque', method='GET')
def saque():
    return ctl.render('withdraw')

# Rota para a página de transferência
@app.route('/transferencia', method='GET')
def transferencia():
    return ctl.render('transfer')

@app.route('/transferencia', method='POST')
def action_transfer():
    return ctl.process_transfer()

@app.route('/saque', method='POST')
def process_withdraw():
    session_id = request.get_cookie('session_id')
    user = ctl.get_current_user(session_id)
    
    if not user:
        return {'success': False, 'message': 'Usuário não autenticado'}

    withdraw_data = request.json
    withdraw_amount = withdraw_data.get('amount')

    if withdraw_amount and withdraw_amount > 0:
        if user.balance >= withdraw_amount:
            user.balance -= withdraw_amount
            ctl.update_user(user)
            return {'success': True}
        else:
            return {'success': False, 'message': 'Saldo insuficiente'}
    else:
        return {'success': False, 'message': 'Valor inválido para saque'}


if __name__ == '__main__':
    run(app, host='localhost', port=9000, debug=True)
