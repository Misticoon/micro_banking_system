// Verificação para o formulário de registro
if (document.getElementById('registerForm')) {
    document.getElementById('registerForm').addEventListener('submit', function(event) {
        event.preventDefault();
        
        // Obter valores dos campos do formulário
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

        // Redireciona para a página inicial
        window.location.href = "/";
    });
}
