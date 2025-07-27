// frontend/src/api.js
const API_BASE_URL = 'http://localhost:8000'

export const sendMessageToAgent = async (query) => {
    try {
        const response = await fetch(`${API_BASE_URL}/agent`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query }),
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || 'Erreur du serveur');
        }

        const data = await response.json();
        return data.answer;
    } catch (error) {
        console.error('Erreur lors de l\'envoi du message à l\'agent:', error);
        throw error;
    }
};