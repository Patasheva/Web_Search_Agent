from langchain_core.prompts import ChatPromptTemplate
from llm_router import get_llm
from state import ResearchState
from logger import logger 

generate_response_prompt =  """    
Given the following user query and content consisting of a set of summarized article 
snippets—each including one sentence summary and its exact corresponding URL—generate 
a response that directly answers the query using relevant information from the content. 
Ensure the response is clear, concise, and based solely on the information provided in 
the content. Additionally, if the user requests it, include the exact URLs from the 
content in the response.

Query: {query}

Content: {content}

Answer:
"""

def generate_response(state: ResearchState):
    model = get_llm()
    logger.info("Début de la génération de la réponse")
    prompt = ChatPromptTemplate.from_template(generate_response_prompt)
    chain = prompt | model

    content = ""
    for i, summary in enumerate(state["summarized_results"]):
        try:
            source = state["sources"][i]
        except IndexError:
            source = "Source inconnue"
        content += f"{i+1}. {summary}\nSource: {source}\n\n"

    logger.info(f"Contenu contextuel fourni pour la génération de la réponse (premiers 100 chars) : {content[:100]}...")
    
    response = chain.invoke({"query": state["query"], "content": content})
    logger.info("Réponse générée avec succès")

    return {
        "response": response
    }