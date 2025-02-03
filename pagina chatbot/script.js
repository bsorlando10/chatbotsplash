document.getElementById('send-btn').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    
    if (userInput.trim()) {
        // Agregar mensaje del usuario
        const userMessage = document.createElement('div');
        userMessage.classList.add('message', 'user');
        userMessage.textContent = userInput;
        document.getElementById('chat-box').appendChild(userMessage);

        // Limpiar el campo de entrada
        document.getElementById('user-input').value = '';

        // Hacer scroll hacia abajo
        document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight;

        // Enviar el mensaje al servidor usando AJAX
        fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput })
        })
        .then(response => response.json())
        .then(data => {
            // Respuesta del bot
            const botMessage = document.createElement('div');
            botMessage.classList.add('message', 'bot');
            botMessage.textContent = data.response;
            document.getElementById('chat-box').appendChild(botMessage);

            // Hacer scroll hacia abajo
            document.getElementById('chat-box').scrollTop = document.getElementById('chat-box').scrollHeight;
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }
});
