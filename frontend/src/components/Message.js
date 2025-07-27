// frontend/src/components/Message.js
import React from 'react';
import './Message.css'; // Créez ce fichier CSS si vous voulez du style

function Message({ text, sender }) {
  const isUser = sender === 'user';
  return (
    <div className={`message ${isUser ? 'user' : 'assistant'}`}>
      <div className="message-bubble">
        {text}
      </div>
    </div>
  );
}

export default Message;