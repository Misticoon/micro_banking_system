// Simulação de um banco de dados de usuários
const users = [
    { email: "user@example.com", password: "password" },
    { email: "admin@example.com", password: "admin123" }
];

// Verificação para o formulário de login
if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const loginEmail = document.getElementById('loginEmail').value;
        const loginPassword = document.getElementById('loginPassword').value;

        // Verificação se o usuário existe no "banco de dados"
        const userExists = users.find(user => user.email === loginEmail && user.password === loginPassword);

        if (userExists) {
            // Redirecionar para a página principal (usando a rota correta do servidor)
            window.location.href = "/";
        } else {
            // Exibir notificação de erro se o login falhar
            alert("Email ou senha incorretos.");
        }
    });

    // Redireciona para a página de registro
    document.getElementById('registerBtn').addEventListener('click', function() {
        window.location.href = "/register";
    });
}

// Verificação para o formulário de registro
if (document.getElementById('registerForm')) {
    document.getElementById('registerForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Obter valores dos campos do formulário
        const firstName = document.getElementById('firstName').value;
        const lastName = document.getElementById('lastName').value;
        const registerEmail = document.getElementById('registerEmail').value;
        const dob = document.getElementById('registerDob').value;
        const registerPassword = document.getElementById('registerPassword').value;
        const confirmPassword = document.getElementById('registerConfirmPassword').value;
        
        // Calcular idade com base na data de nascimento
        const birthDate = new Date(dob);
        const today = new Date();
        let age = today.getFullYear() - birthDate.getFullYear();
        const monthDifference = today.getMonth() - birthDate.getMonth();
        
        if (monthDifference < 0 || (monthDifference === 0 && today.getDate() < birthDate.getDate())) {
            age--;
        }

        // Verificação se o usuário tem menos de 18 anos
        if (age < 18) {
            alert('Você deve ter pelo menos 18 anos para se registrar.');
            return; // Interrompe o envio do formulário
        }

        // Verificação se as senhas coincidem
        if (registerPassword !== confirmPassword) {
            alert('As senhas não coincidem. Por favor, verifique.');
            return; // Interrompe o envio do formulário
        }

        // Adicionar o novo usuário ao "banco de dados"
        users.push({ email: registerEmail, password: registerPassword });

        // Exibe uma caixa de aviso ao usuário
        alert('Cadastro realizado com sucesso! Redirecionando para a página inicial.');

        // Redireciona para a página inicial (usando a rota correta do servidor)
        window.location.href = "/";
    });
}

// Função de Logout
if (document.getElementById('logoutBtn')) {
    document.getElementById('logoutBtn').addEventListener('click', function() {
        alert("Você saiu da conta.");
        // Redirecionar para a página de login
        window.location.href = "/";
    });
}

// Funcionalidade de depósito
if (document.getElementById('depositBtn')) {
    document.getElementById('depositBtn').addEventListener('click', function() {
        // Verifica se está na página de depósito ou redireciona para ela
        if (document.getElementById('depositValue')) {
            const depositValue = document.getElementById('depositValue').value;
            if (depositValue) {
                alert(`Depósito de R$ ${depositValue} realizado com sucesso!`);
            } else {
                alert("Por favor, insira um valor para o depósito.");
            }
        } else {
            window.location.href = "/deposito";
        }
    });

    // Limpar o valor do depósito
    if (document.getElementById('clearBtn')) {
        document.getElementById('clearBtn').addEventListener('click', function() {
            document.getElementById('depositValue').value = '';
        });
    }
}

// Funcionalidade de saque
if (document.getElementById('withdrawBtn')) {
    document.getElementById('withdrawBtn').addEventListener('click', function() {
        // Verifica se está na página de saque ou redireciona para ela
        if (document.getElementById('withdrawValue')) {
            const withdrawValue = document.getElementById('withdrawValue').value;
            if (withdrawValue) {
                alert(`Saque de R$ ${withdrawValue} realizado com sucesso!`);
            } else {
                alert("Por favor, insira um valor para o saque.");
            }
        } else {
            window.location.href = "/saque";
        }
    });

    // Limpar o valor do saque
    if (document.getElementById('clearBtn')) {
        document.getElementById('clearBtn').addEventListener('click', function() {
            document.getElementById('withdrawValue').value = '';
        });
    }
}

// Funcionalidade de transferência
if (document.getElementById('transferBtn')) {
    document.getElementById('transferBtn').addEventListener('click', function() {
        // Verifica se está na página de transferência ou redireciona para ela
        if (document.getElementById('destinationAccount') && document.getElementById('transferValue')) {
            const destinationAccount = document.getElementById('destinationAccount').value;
            const transferValue = document.getElementById('transferValue').value;
            
            if (destinationAccount && transferValue) {
                alert(`Transferência de R$ ${transferValue} para a conta ${destinationAccount} realizada com sucesso!`);
            } else {
                alert("Por favor, insira o número da conta de destino e o valor da transferência.");
            }
        } else {
            window.location.href = "/transferencia";
        }
    });

    // Limpar os campos de transferência
    if (document.getElementById('clearBtn')) {
        document.getElementById('clearBtn').addEventListener('click', function() {
            document.getElementById('destinationAccount').value = '';
            document.getElementById('transferValue').value = '';
        });
    }
}
