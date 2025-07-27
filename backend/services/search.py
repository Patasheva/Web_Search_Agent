from langchain_community.utilities import SerpAPIWrapper
from config import SERPAPI_API_KEY
from state import ResearchState
from logger import logger  

def search_web(state: ResearchState):
    query = state["query"]
    logger.info(f"🔍 Lancement de la recherche web pour : '{query}'")

    try:
        search = SerpAPIWrapper(
            serpapi_api_key=SERPAPI_API_KEY,
            params={"tbs": "qdr:w"}  # week
        )

        raw_search_results = search.results(query) # JSON
        search_results = raw_search_results.get("organic_results", [])[:3]

        logger.info(f"✅ {len(search_results)} résultats trouvés")

        return {
            "sources": [result.get("link") for result in search_results],
            "web_results": [result.get("snippet") for result in search_results]
        }

    except Exception as e:
        logger.error(f"❌ Erreur lors de la recherche : {e}")
        raise