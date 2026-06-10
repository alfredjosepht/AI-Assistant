from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("DocumentServer")


@mcp.tool()
def list_documents():

    return os.listdir("documents")


@mcp.tool()
def read_document(filename: str):

    path = os.path.join(
        "documents",
        filename
    )

    if not os.path.exists(path):
        return "File not found"

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        return file.read()


if __name__ == "__main__":

    print("Document Server Started")
    mcp.run()