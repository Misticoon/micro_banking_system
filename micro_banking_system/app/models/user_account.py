class UserAccount:
    def __init__(self, first_name, last_name, email, password, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.dob = dob

    def validate_password(self):
        # Adicione lógica de validação de senha aqui, se necessário
        if len(self.password) < 8:
            return False
        return True

    def validate_email(self):
        # Simples validação de formato de e-mail
        if "@" in self.email and "." in self.email:
            return True
        return False

    def register(self):
        if not self.validate_email():
            return "Email inválido!"
        if not self.validate_password():
            return "A senha deve ter pelo menos 8 caracteres!"
        
        # Simulação de registro, normalmente aqui você salvaria em um banco de dados
        print(f"Usuário registrado: {self.first_name} {self.last_name}, Email: {self.email}, Data de Nascimento: {self.dob}")
        return "Registro bem-sucedido!"

    def who_r_u(self):
        print(f"Nome: {self.first_name} {self.last_name}, Email: {self.email}")
