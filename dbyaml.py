import yaml


def load_library(file):
    """
    Loads library from .yaml file.
    :param file: file name.
    :returns a list of books in case of success, or empty list otherwise.
    """
    try:
        with open(file, "r") as opened_file:
            return yaml.load(opened_file.read())
    except FileNotFoundError:
        return []


def save_library(file, catalogue):
    """
    Dumps library into .yaml file.
    :param file: file name.
    :param catalogue: a list of books.
    :returns catalogue in case of success.
    """
    with open(file, "w") as opened_file:
        yaml.dump(catalogue, opened_file)
        return catalogue


if __name__ == "__main__":
    books = load_library("test.yaml")
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
    if save_library("test.yaml", books) == 0:
        print("OK")
    else:
        print("Fail")
