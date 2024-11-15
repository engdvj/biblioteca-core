// Função para obter o token CSRF do cookie
function getCSRFToken() {
    let csrfToken = null;
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
        if (cookie.trim().startsWith('csrftoken=')) {
            csrfToken = cookie.trim().substring('csrftoken='.length);
            break;
        }
    }
    return csrfToken;
}

function submitLogin() {
    console.log('Função submitLogin chamada');
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const csrfToken = getCSRFToken();

    fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken,
        },
        body: JSON.stringify({ username, password }),  // Envia as credenciais
    })
    .then(response => response.json())
    .then(data => {
        if (data.token) {
            localStorage.setItem('token', data.token);
            console.log(`Token de autenticação recebido: ${data.token}`);
            fetchProtectedData();
            window.location.href = '/api/';
        } else {
            alert('Credenciais inválidas');
        }
    })
    .catch(error => console.error('Erro:', error));
}


// Função para buscar dados protegidos
function fetchProtectedData() {
    console.log('Função fetchProtectedData chamada');

    // Recupera o token do localStorage
    const token = localStorage.getItem('token');

    if (!token) {
        console.error('Token não encontrado!');
        return;
    }

    // Faz uma requisição GET para /api/ com o token no cabeçalho Authorization
    fetch('/api/', {
        method: 'GET',
        headers: {
            'Authorization': `Token ${token}`, // Adiciona o token no cabeçalho
            'Content-Type': 'application/json',
        },
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error('Falha na autenticação');
        }
    })
    .then(data => {
        console.log('Dados protegidos:', data);
    })
    .catch(error => console.error('Erro:', error));
}
