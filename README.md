# Assistant IA 🔎 Recherche Web 
Un chatbot simple capable d’accéder à Internet pour rechercher des informations et générer des réponses pertinentes en s’appuyant sur des contenus fiables et récents. Il accède au moteur de recherche Google, filtre les pages par mots-clés et par date, extrait un court résumé de chaque page ainsi que le lien vers la source, puis intègre ces informations dans la réponse générée.

# Stack technique
- Backend : Python, FastAPI
- Frontend : React
- Web search : SerpAPI

# LLMs open source
- qwen-2.5-72b-instruct (via OpenRouter)
- mistral:7b (en local via Ollama)

# Orchestration 
- LangGraph
- Architecture modulaire

# Prérequis
- installer ollama en local (https://ollama.com)
- télécharger mistral en local: ollama pull mistral:7b
- SERPAPI_API_KEY
- OPENROUTER_API_KEY

# Déploiement sur Azure
- Prérequis techniques
✔️ Compte Azure actif avec une souscription
✔️ Docker installé (pour conteneuriser backend et frontend)
✔️ GitHub ou Azure DevOps pour CI/CD
✔️ Nom de domaine (optionnel) via Azure DNS

# App Services Azure
  - Web App pour déployer le backend via GitHub (via code et via conteneur Docker)
  - Static Web App pour déployer le frontend via Github code 
  - Azure Key Vault: stocker les secrets et API keys.
  - Azure Monitor: monitoting post-deployement et gestion des erreurs  

Étape 3 – Déploiement (en résumé)

Conteneuriser le backend FastAPI avec Docker
Build du frontend React en production (npm run build)
Pousser le projet sur GitHub
Connecter GitHub à Azure App Services via GitHub Actions
Configurer les variables d’environnement et clés dans Azure Key Vault
Déployer automatiquement à chaque push



