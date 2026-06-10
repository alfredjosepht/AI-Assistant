import os
import json
import asyncio

from dotenv import load_dotenv

from mcp import ClientSession
from mcp.client.stdio import (
    stdio_client,
    StdioServerParameters
)

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def get_server_params():

    return StdioServerParameters(
        command="npx",
        args=[
            "@modelcontextprotocol/server-github"
        ],
        env={
            "GITHUB_PERSONAL_ACCESS_TOKEN":
            GITHUB_TOKEN
        }
    )


async def get_tools():

    server_params = get_server_params()

    async with stdio_client(
        server_params
    ) as (
        read_stream,
        write_stream
    ):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            await session.initialize()

            tools = await session.list_tools()

            return [
                tool.name
                for tool in tools.tools
            ]


async def search_repo(query):

    server_params = get_server_params()

    async with stdio_client(
        server_params
    ) as (
        read_stream,
        write_stream
    ):

        async with ClientSession(
            read_stream,
            write_stream
        ) as session:

            await session.initialize()

            result = await session.call_tool(
                "search_repositories",
                {
                    "query": query
                }
            )

            try:

                raw_text = (
                    result.content[0].text
                )

                data = json.loads(
                    raw_text
                )

                repos = data.get(
                    "items",
                    []
                )[:5]

                if not repos:
                    return (
                        "No repositories found."
                    )

                output = (
                    "\n=== GitHub Search Results ===\n\n"
                )

                for i, repo in enumerate(
                    repos,
                    start=1
                ):

                    output += (
                        f"{i}. {repo['full_name']}\n"
                        f"Description: "
                        f"{repo.get('description', 'No description')}\n"
                        f"Stars: "
                        f"{repo.get('stargazers_count', 0)}\n"
                        f"URL: "
                        f"{repo['html_url']}\n\n"
                    )

                return output

            except Exception:

                return str(result)


if __name__ == "__main__":

    print(
        "\nGitHub MCP Test\n"
    )

    tools = asyncio.run(
        get_tools()
    )

    print(
        "\nAvailable Tools:\n"
    )

    for tool in tools:

        print(tool)