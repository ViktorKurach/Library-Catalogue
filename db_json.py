import json


def load_library(file):
    """
    Loads library from .json file.
    :param file: file object.
    :returns a list of books in case of success, or empty list otherwise.
    """
    with file:
        return json.loads(file.read())


def dump_library(file, catalogue):
    """
    Dumps library into .json file.
    :param file: file object.
    :param catalogue: a list of books.
    :returns catalogue in case of success.
    """
    with file:
        json.dump(catalogue, file)
        return catalogue
