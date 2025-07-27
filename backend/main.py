from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent_graph import graph
from fastapi.responses import JSONResponse

app = FastAPI(title="Web Search Agent")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    answer: str

# Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/agent", response_model=QueryResponse)
async def run_agent(request: QueryRequest):
    try:
        state = graph.invoke({"query": request.query})
        print("🧪 Contenu de state:", state)

        # Récupère la réponse depuis AIMessage
        answer = state["response"].content

        return QueryResponse(answer=answer)

    except Exception as e:
        print("🔥 Erreur dans /agent:", e)
        raise HTTPException(status_code=500, detail=str(e))