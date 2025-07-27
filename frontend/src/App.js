// frontend/src/App.js
import React, { useState, useEffect, useRef } from 'react';
import Message from './components/Message';
import ChatInput from './components/ChatInput';
import { sendMessageToAgent } from './api';
import './App.css'; // Pour le style global

function App() {
  const [messages, setMessages] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (query) => {
    const newUserMessage = { id: messages.length, text: query, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, newUserMessage]);
    setIsLoading(true);

    try {
      const agentResponse = await sendMessageToAgent(query);
      const newAgentMessage = { id: messages.length + 1, text: agentResponse, sender: 'assistant' };
      setMessages((prevMessages) => [...prevMessages, newAgentMessage]);
    } catch (error) {
      const errorMessage = { id: messages.length + 1, text: `Erreur: ${error.message}`, sender: 'assistant' };
      setMessages((prevMessages) => [...prevMessages, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Assistant IA 🔍 Recherche Web</h1>
      </header>
      <div className="chat-window">
        <div className="messages-container">
          {messages.length === 0 && (
            <div className="welcome-message">
               Pose-moi ta question 👇 Je cherche pour toi les infos les plus récentes sur Google!
            </div>
          )}
          {messages.map((msg) => (
            <Message key={msg.id} text={msg.text} sender={msg.sender} />
          ))}
          {isLoading && (
            <Message text="Recherche en cours…" sender="assistant" />
          )}
          <div ref={messagesEndRef} />
        </div>
        <ChatInput onSendMessage={handleSendMessage} isLoading={isLoading} />
      </div>
    </div>
  );
}

export default App;
