document.getElementById('logoutBtn').addEventListener('click', function() {
    alert("Você saiu da conta.");
    // Redirecionar para a página de login
    window.location.href = "index.html";
});

document.getElementById('clearBtn').addEventListener('click', function() {
    // Limpa o valor do depósito
    document.getElementById('depositValue').value = '';
});

document.getElementById('depositBtn').addEventListener('click', function() {
    // Lógica de depósito (a ser implementada)
    const depositValue = document.getElementById('depositValue').value;
    if (depositValue) {
        alert(`Depósito de R$ ${depositValue} realizado com sucesso!`);
    } else {
        alert("Por favor, insira um valor para o depósito.");
    }
});
