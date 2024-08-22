// Verificação para o formulário de login
if (document.getElementById('loginForm')) {
    document.getElementById('loginForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const loginEmail = document.getElementById('loginEmail').value;
        const loginPassword = document.getElementById('loginPassword').value;

        const form = document.getElementById('loginForm');
        form.submit(); // Submete o formulário ao backend para autenticação

    });

    document.getElementById('registerBtn').addEventListener('click', function() {
        window.location.href = "/register";
    });
}

// Verificação para o formulário de registro
if (document.getElementById('registerForm')) {
    document.getElementById('registerForm').addEventListener('submit', function(event) {
        // Obter valores dos campos do formulário
        const registerEmail = document.getElementById('registerEmail').value;
        
        // Verificação se o email já existe no "banco de dados"
        const emailExists = users.some(function(user) {
            return user.email === registerEmail;
        });

        if (emailExists) {
            alert('O email informado já está registrado. Por favor, use outro email.');
            event.preventDefault(); // Impede o envio do formulário se o email já existir
            return;
        }

        // Outras validações...
    });
}


// Função de Logout
if (document.getElementById('logoutBtn')) {
    document.getElementById('logoutBtn').addEventListener('click', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        fetch('/logout', { method: 'POST' })
            .then(response => {
                if (response.ok) {
                    window.location.href = "/";
                } else {
                    alert("Erro ao tentar fazer logout. Tente novamente.");
                }
            })
            .catch(error => console.error('Erro:', error));
    });
}


// Funcionalidade de depósito
document.getElementById('depositBtn').addEventListener('click', function() {
    window.location.href = "/deposito";
});

// Funcionalidade de saque
document.getElementById('withdrawBtn').addEventListener('click', function() {
    window.location.href = "/saque";
});

// Funcionalidade de transferência
document.getElementById('transferBtn').addEventListener('click', function() {
    window.location.href = "/transferencia";
});
