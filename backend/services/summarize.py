from langchain_core.prompts import ChatPromptTemplate
from llm_router import get_llm
from clean_text import clean_text
from state import ResearchState
from logger import logger 

summary_prompt = """
You are given three short content snippets retrieved from a web search. For each one, write a single clear and concise 
sentence summarizing the main idea of the snippet. Each sentence should stand alone and reflect the most relevant 
information related to the user query.

Query: {query}
Content: {content}
"""

def summarize_results(state: ResearchState):
    logger.info("Démarrage de la fonction summarize_results")
    model = get_llm()
    prompt = ChatPromptTemplate.from_template(summary_prompt)
    chain = prompt | model

    summarized_results = []
    for content in state["web_results"]:
        logger.info(f"Résumé du contenu : {content[:50]}...") 
        summary = chain.invoke({"query": state["query"], "content": content})
        clean_content = clean_text(summary.content)
        summarized_results.append(clean_content)
    
    logger.info("Résumé terminé, nombre de résumés : %d", len(summarized_results))
    return {
        "summarized_results": summarized_results
    }
