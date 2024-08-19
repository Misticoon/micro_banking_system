// Simulação de um banco de dados de usuários
const users = [
    { email: "user@example.com", password: "password" },
    { email: "admin@example.com", password: "admin123" }
];

document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    // Verificação se o usuário existe no "banco de dados"
    const userExists = users.find(user => user.email === email && user.password === password);

    if (userExists) {
        // Redirecionar para a página "home.html" se o login for bem-sucedido
        window.location.href = "home.html";
    } else {
        // Exibir notificação de erro se o login falhar
        alert("Email ou senha incorretos.");
    }
});

document.getElementById('registerBtn').addEventListener('click', function() {
    // Redireciona para a página de registro
    window.location.href = "register.html";
});