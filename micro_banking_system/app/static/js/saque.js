document.getElementById('logoutBtn').addEventListener('click', function() {
    alert("Você saiu da conta.");
    // Redirecionar para a página de login
    window.location.href = "index.html";
});

document.getElementById('clearBtn').addEventListener('click', function() {
    // Limpa o valor do saque
    document.getElementById('withdrawValue').value = '';
});

document.getElementById('withdrawBtn').addEventListener('click', function() {
    // Lógica de saque (a ser implementada)
    const withdrawValue = document.getElementById('withdrawValue').value;
    if (withdrawValue) {
        alert(`Saque de R$ ${withdrawValue} realizado com sucesso!`);
    } else {
        alert("Por favor, insira um valor para o saque.");
    }
});
