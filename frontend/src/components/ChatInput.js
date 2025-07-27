// frontend/src/components/ChatInput.js
import React, { useState } from 'react';
import './ChatInput.css'; // Créez ce fichier CSS si vous voulez du style

function ChatInput({ onSendMessage, isLoading }) {
  const [input, setInput] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (input.trim() && !isLoading) {
      onSendMessage(input);
      setInput('');
    }
  };

  return (
    <form className="chat-input-form" onSubmit={handleSubmit}>
      <input
        type="text"
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Poser une question"
        disabled={isLoading}
      />
      <button type="submit" disabled={isLoading}>
        {isLoading ? 'Envoi...' : 'Envoyer'}
      </button>
    </form>
  );
}

export default ChatInput;