// LifeHub AI Assistant JavaScript

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    const chatInput = document.getElementById('aiChatInput');
    const sendBtn = document.getElementById('aiSendBtn');
    
    // Enter key to send message
    if (chatInput) {
        chatInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                sendMessage();
            }
        });
    }
});

// Send message function
function sendMessage() {
    const chatInput = document.getElementById('aiChatInput');
    const message = chatInput.value.trim();
    
    if (!message) return;
    
    // Add user message to chat
    addUserMessage(message);
    
    // Clear input
    chatInput.value = '';
    
    // Show loading
    showLoading();
    
    // Send to backend
    fetch('/ai-chat/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        hideLoading();
        if (data.response) {
            addBotMessage(data.response);
        } else {
            addBotMessage('Kechirasiz, xatolik yuz berdi. Qaytadan urinib ko\'ring.');
        }
    })
    .catch(error => {
        hideLoading();
        addBotMessage('Aloqa xatoligi. Iltimos, qaytadan urinib ko\'ring.');
        console.error('Error:', error);
    });
}

// Send quick message
function sendQuickMessage(text) {
    const chatInput = document.getElementById('aiChatInput');
    chatInput.value = text;
    sendMessage();
}

// Add user message to chat
function addUserMessage(message) {
    const chatMessages = document.getElementById('aiChatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'ai-message ai-message-user';
    messageDiv.innerHTML = `
        <div class="ai-message-content">
            <p>${escapeHtml(message)}</p>
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

// Add bot message to chat
function addBotMessage(message) {
    const chatMessages = document.getElementById('aiChatMessages');
    const messageDiv = document.createElement('div');
    messageDiv.className = 'ai-message ai-message-bot';
    messageDiv.innerHTML = `
        <div class="ai-message-content">
            <p>${formatBotMessage(message)}</p>
        </div>
    `;
    chatMessages.appendChild(messageDiv);
    scrollToBottom();
}

// Show loading animation
function showLoading() {
    const chatMessages = document.getElementById('aiChatMessages');
    const loadingDiv = document.createElement('div');
    loadingDiv.className = 'ai-message ai-message-bot ai-loading';
    loadingDiv.id = 'aiLoading';
    loadingDiv.innerHTML = `
        <div class="ai-message-content">
            <div class="ai-loading-dots">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    `;
    chatMessages.appendChild(loadingDiv);
    scrollToBottom();
    
    // Disable send button
    const sendBtn = document.getElementById('aiSendBtn');
    if (sendBtn) {
        sendBtn.disabled = true;
    }
}

// Hide loading animation
function hideLoading() {
    const loadingDiv = document.getElementById('aiLoading');
    if (loadingDiv) {
        loadingDiv.remove();
    }
    
    // Enable send button
    const sendBtn = document.getElementById('aiSendBtn');
    if (sendBtn) {
        sendBtn.disabled = false;
    }
}

// Scroll to bottom of chat
function scrollToBottom() {
    const chatMessages = document.getElementById('aiChatMessages');
    chatMessages.scrollTop = chatMessages.scrollHeight;
}

// Escape HTML to prevent XSS
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// Format bot message with line breaks
function formatBotMessage(message) {
    return escapeHtml(message).replace(/\n/g, '<br>');
}