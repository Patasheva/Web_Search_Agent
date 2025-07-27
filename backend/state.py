from typing_extensions import TypedDict

class ResearchState(TypedDict):
    query: str
    sources: list[str]
    web_results: list[str]
    summarized_results: list[str]
    response: str

class ResearchStateInput(TypedDict):
    query: str

class ResearchStateOutput(TypedDict):
    sources: list[str]
    response: str