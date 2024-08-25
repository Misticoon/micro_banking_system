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

    // Verificação de erro de login através do cookie
    document.addEventListener('DOMContentLoaded', function() {
        // Função para obter o valor de um cookie específico
        function getCookie(name) {
            const value = `; ${document.cookie}`;
            const parts = value.split(`; ${name}=`);
            if (parts.length === 2) return parts.pop().split(';').shift();
        }

        const loginError = getCookie('login_error');

        if (loginError) {
            alert('Falha no login. Verifique suas credenciais e tente novamente.');

            // Remove o cookie após mostrar o alerta
            document.cookie = "login_error=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
        }
    });
}


// Verificação para o formulário de registro
if (document.getElementById('registerForm')) {
    document.getElementById('registerForm').addEventListener('submit', function(event) {
        const registerEmail = document.getElementById('registerEmail').value;
        const registerPassword = document.getElementById('registerPassword').value;
        const registerConfirmPassword = document.getElementById('registerConfirmPassword').value;
        const registerDob = new Date(document.getElementById('registerDob').value);
        const today = new Date();
        
        // Cálculo da idade
        let age = today.getFullYear() - registerDob.getFullYear();
        const monthDiff = today.getMonth() - registerDob.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < registerDob.getDate())) {
            age--;
        }

        // Verifica se as senhas são iguais
        if (registerPassword !== registerConfirmPassword) {
            alert('As senhas não coincidem. Por favor, verifique e tente novamente.');
            event.preventDefault();
            return;
        }

        // Verifica se o usuário tem pelo menos 18 anos
        if (age < 18) {
            alert('Você deve ter pelo menos 18 anos para se registrar.');
            event.preventDefault();
            return;
        }

        // Verificação do email já existente é feita no servidor, exibido no frontend
        event.preventDefault();
        fetch(`/email_exists?email=${encodeURIComponent(registerEmail)}`)
            .then(response => response.json())
            .then(data => {
                if (data.exists) {
                    alert('O email informado já está registrado. Por favor, use outro email.');
                } else {
                    alert('Cadastro realizado com sucesso!');
                    document.getElementById('registerForm').submit();
                }
            })
            .catch(error => console.error('Erro:', error));
    });
}




// Função de Logout
if (document.getElementById('logoutBtn')) {
    document.getElementById('logoutBtn').addEventListener('click', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        fetch('/logout', { method: 'POST' })
            .then(response => {
                if (response.ok) {
                    alert("Você saiu com sucesso!"); // Mensagem de sucesso
                    window.location.href = "/";
                } else {
                    alert("Erro ao tentar fazer logout. Tente novamente.");
                }
            })
            .catch(error => console.error('Erro:', error));
    });
}



// Verificação para o formulário de login
// ... (outros scripts existentes)

// Verifique se o botão de Home está presente na página
if (document.querySelector('.home-icon a')) {
    document.querySelector('.home-icon a').addEventListener('click', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        window.location.href = "/home"; // Redireciona para /home
    });
}

// Verifica se o ícone de retorno está presente na página
if (document.querySelector('.return-icon a')) {
    document.querySelector('.return-icon a').addEventListener('click', function(event) {
        event.preventDefault(); // Impede o comportamento padrão do link
        window.location.href = "/"; // Redireciona para /index
    });
}

document.addEventListener('DOMContentLoaded', function() {
    const depositBtn = document.getElementById('depositBtn');
    const withdrawBtn = document.getElementById('withdrawBtn');
    const transferBtn = document.getElementById('transferBtn');
    const clearBtn = document.getElementById('clearBtn');

    if (depositBtn) {
        depositBtn.addEventListener('click', function() {
            const depositValue = parseFloat(document.getElementById('depositValue').value);

            if (depositValue > 0) {
                fetch('/deposito', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ amount: depositValue })
                })
                .then(response => {
                    console.log('Resposta recebida:', response);  // Adiciona log para depuração
                    if (!response.ok) {
                        throw new Error('Erro ao processar a solicitação');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log('Dados recebidos:', data);  // Adiciona log para depuração
                    if (data.success) {
                        alert('Depósito realizado com sucesso!');
                    } else {
                        alert('Erro ao realizar depósito: ' + data.message);
                    }
                    window.location.href = "/deposito";
                })
                .catch(error => {
                    console.error('Erro:', error);
                    alert('Erro ao realizar depósito. Tente novamente mais tarde.');
                    window.location.href = "/deposito";
                });                              
            } else {
                alert('Por favor, insira um valor válido para o depósito.');
            }
        });
    }

    if (withdrawBtn) {
        withdrawBtn.addEventListener('click', function() {
            const withdrawValue = parseFloat(document.getElementById('withdrawValue').value);

            if (withdrawValue > 0) {
                fetch('/saque', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ amount: withdrawValue })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Saque realizado com sucesso!');
                    } else {
                        alert('Erro ao realizar saque: ' + data.message);
                    }
                    window.location.href = "/saque";
                })
                .catch(error => {
                    console.error('Erro:', error);
                    alert('Erro ao realizar saque. Tente novamente mais tarde.');
                    window.location.href = "/saque";
                });
            } else {
                alert('Por favor, insira um valor válido para o saque.');
            }
        });
    }

    if (transferBtn) {
        transferBtn.addEventListener('click', function() {
            const destinationAccount = document.getElementById('destinationAccount').value;
            const transferValue = parseFloat(document.getElementById('transferValue').value);

            if (transferValue > 0 && destinationAccount) {
                fetch('/transferencia', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({ destinationAccount, amount: transferValue })
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert('Transferência realizada com sucesso!');
                    } else {
                        alert('Erro ao realizar transferência: ' + data.message);
                    }
                    window.location.href = "/transferencia";
                })
                .catch(error => {
                    console.error('Erro:', error);
                    alert('Erro ao realizar transferência. Tente novamente mais tarde.');
                    window.location.href = "/transferencia";
                });
            } else {
                alert('Por favor, insira um valor válido e uma conta de destino.');
            }
        });
    }

    if (clearBtn) {
        clearBtn.addEventListener('click', function() {
            if (document.body.classList.contains('transferencia')) {
                document.getElementById('destinationAccount').value = '';
                document.getElementById('transferValue').value = '';
            } else if (document.body.classList.contains('saque')) {
                document.getElementById('withdrawValue').value = '';
            } else if (document.body.classList.contains('deposito')) {
                document.getElementById('depositValue').value = '';
            }
        });
    }
});


// Funcionalidade de depósito
document.getElementById('depositPageBtn').addEventListener('click', function() {
    window.location.href = "/deposito";
});

// Funcionalidade de saque
document.getElementById('withdrawPageBtn').addEventListener('click', function() {
    window.location.href = "/saque";
});

// Funcionalidade de transferência
document.getElementById('transferPageBtn').addEventListener('click', function() {
    window.location.href = "/transferencia";
});

