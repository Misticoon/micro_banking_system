document.getElementById('logoutBtn').addEventListener('click', function() {
    alert("Você saiu da conta.");
    // Redirecionar para a página de login
    window.location.href = "index.html";
});

document.getElementById('depositBtn').addEventListener('click', function() {
    // Redireciona para a página de depósito
    window.location.href = "deposito.html";
});

document.getElementById('withdrawBtn').addEventListener('click', function() {
    // Redireciona para a página de saque
    window.location.href = "saque.html";
});

document.getElementById('transferBtn').addEventListener('click', function() {
    // Redireciona para a página de transferência
    window.location.href = "transferencia.html";
});