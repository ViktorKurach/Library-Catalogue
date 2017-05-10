import json


def load_library(file):
    """
    Loads library from .json file.
    :param file: file name.
    :returns a list of books in case of success, or empty list otherwise.
    """
    try:
        with open(file, "rb") as opened_file:
            return json.loads(opened_file.read())
    except FileNotFoundError:
        return []


def save_library(file, catalogue):
    """
    Dumps library into .json file.
    :param file: file name.
    :param catalogue: a list of books.
    :returns catalogue in case of success.
    """
    with open(file, "w") as opened_file:
        opened_file.write(json.dumps(catalogue))
        return catalogue


if __name__ == "__main__":
    books = load_library("test.json")
    if books:
        print("OK")
    else:
        print("Fail")
        books = [{"path": "Path", "title": "T1", "author": "A1",
                  "publication": "P", "genre": "G", "description": "D",
                  "year": 1900},
                 {"path": "Path", "title": "T2", "author": "A2",
                  "publication": "P", "genre": "G", "description": "D",
                  "year": 2000},
                 {"path": "Path", "title": "T3", "author": "A2",
                  "publication": "P", "genre": "G", "description": "D",
                  "year": 2010}]
    print(books)
    if save_library("test.json", books) == 0:
        print("OK")
    else:
        print("Fail")
