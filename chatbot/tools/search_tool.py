from chatbot.llm import model
from ddgs import DDGS


def web_search(query):

    with DDGS() as ddgs:

        results = list(
            ddgs.text(
                query,
                max_results=5
            )
        )

    if not results:
        return "No results found."

    context = ""

    for result in results:

        context += (
            result["title"]
            + "\n"
            + result["body"]
            + "\n\n"
        )

    prompt = f"""
Summarize these search results.

{context}
"""

    response = model.invoke(prompt)

    return response.content