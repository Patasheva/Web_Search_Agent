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
  
# Mode local
Terminal 1 (backend): uvicorn main:app --reload
http://localhost:8000
Terminal 2 (frontend): npm start 
http://localhost:3000



