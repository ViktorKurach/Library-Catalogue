import pickle


def load_library(file):
    """
    Loads library from .pkl file.
    :param file: file object.
    :returns a list of books in case of success, or empty list otherwise.
    """
    with file:
        return pickle.loads(file.read())


def dump_library(file, catalogue):
    """
    Dumps library into .pkl file.
    :param file: file object.
    :param catalogue: a list of books.
    :returns catalogue in case of success.
    """
    with file:
        file.write(pickle.dumps(catalogue))
        return catalogue
