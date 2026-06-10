import os


def list_documents():

    return os.listdir("documents")


def read_document(filename):

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