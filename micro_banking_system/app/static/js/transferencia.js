document.getElementById('logoutBtn').addEventListener('click', function() {
    alert("Você saiu da conta.");
    // Redirecionar para a página de login
    window.location.href = "index.html";
});

document.getElementById('clearBtn').addEventListener('click', function() {
    // Limpa os campos de número da conta de destino e valor da transferência
    document.getElementById('destinationAccount').value = '';
    document.getElementById('transferValue').value = '';
});

document.getElementById('transferBtn').addEventListener('click', function() {
    // Lógica de transferência (a ser implementada)
    const destinationAccount = document.getElementById('destinationAccount').value;
    const transferValue = document.getElementById('transferValue').value;
    
    if (destinationAccount && transferValue) {
        alert(`Transferência de R$ ${transferValue} para a conta ${destinationAccount} realizada com sucesso!`);
    } else {
        alert("Por favor, insira o número da conta de destino e o valor da transferência.");
    }
});
