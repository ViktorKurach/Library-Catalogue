import pickle


def load_library(file):
    """
    Loads library from .pkl file.
    :param file: file name.
    :returns a list of books in case of success, or empty list otherwise.
    """
    try:
        with open(file, "rb") as opened_file:
            return pickle.load(opened_file)
    except FileNotFoundError:
        return []


def save_library(file, catalogue):
    """
    Dumps library into .pkl file.
    :param file: file name.
    :param catalogue: a list of books.
    :returns catalogue in case of success.
    """
    with open(file, "wb") as opened_file:
        pickle.dump(catalogue, opened_file)
        return catalogue


if __name__ == "__main__":
    books = load_library("test.pkl")
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
    if save_library("test.pkl", books) == 0:
        print("OK")
    else:
        print("Fail")