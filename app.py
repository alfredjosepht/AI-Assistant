from chatbot.chatbot import (
    get_response,
    extract_person,
    extract_datetime
)
from chatbot.mcp.client import (
    list_documents,
    read_document
)
import asyncio

from chatbot.mcp.github_client import (
    get_tools,
    search_repo
)
from chatbot.tools.calculator_tool import calculator
from chatbot.tools.time_tool import current_time
from chatbot.tools.memory_tool import show_memory
from chatbot.tools.wiki_tool import search_wikipedia
from chatbot.tools.search_tool import web_search


print("AI Assistant Started")
print("Type exit to quit\n")

print("Available Commands:")
print("/extract_person")
print("/extract_time")
print("/calc")
print("/time")
print("/memory")
print("/wiki")
print("/search")
print("/docs")
print("/read")
print("/github_tools")
print("/gh_search")
print()


while True:

    user_input = input("Alfred: ")

    # Exit
    if user_input.lower() == "exit":
        break

    # Person Parser
    if user_input.lower() == "/extract_person":

        text = input(
            "\nEnter text: "
        )

        result = extract_person(
            text
        )

        print("\nParsed Data:")
        print(result)
        print()

        continue

    # Datetime Parser
    if user_input.lower() == "/extract_time":

        text = input(
            "\nEnter text: "
        )

        result = extract_datetime(
            text
        )

        print("\nParsed Data:")
        print(result)
        print()

        continue

    # Calculator Tool
    if user_input.lower() == "/calc":

        expression = input(
            "\nExpression: "
        )

        result = calculator(
            expression
        )

        print("\nResult:")
        print(result)
        print()

        continue

    # Current Time Tool
    if user_input.lower() == "/time":

        print("\nCurrent Time:")
        print(current_time())
        print()

        continue

    # Memory Tool
    if user_input.lower() == "/memory":

        print("\nChat Memory:")
        print(show_memory())
        print()

        continue
    if user_input.lower() == "/wiki":

        query = input(
        "\nSearch Wikipedia: ")
        result = search_wikipedia(query)

        print("\nWikipedia Result:")
        print(result)
        print()

        continue
    if user_input.lower() == "/search":

        query = input("\nSearch Query: ")
        result = web_search(query)

        print("\nSearch Results:")
        print(result)
        print()
        continue
    if user_input.lower() == "/docs":

        docs = list_documents()

        print("\nDocuments:\n")

        for doc in docs:
            print(doc)

        print()

        continue
    if user_input.lower() == "/read":

        filename = input(
            "\nFilename: "
        )

        content = read_document(
            filename
        )

        print("\nContent:\n")

        print(content)

        print()

        continue
    if user_input.lower() == "/github_tools":

        tools = asyncio.run(
            get_tools()
        )

        print("\nGitHub MCP Tools:\n")

        for tool in tools:
            print(tool)

        print()

        continue
    if user_input.lower() == "/gh_search":

        query = input(
            "\nRepository Search: "
        )

        result = asyncio.run(
            search_repo(query)
        )

        print("\nResult:\n")

        print(result)

        print()

        continue
    # Normal Chat
    print("\nAI: ", end="")

    get_response(user_input)

    print("\n")