import yaml


def load_library(file):
    """
    Loads library from .yaml file.
    :param file: file object.
    :returns a list of books in case of success, or empty list otherwise.
    """
    with file:
        return yaml.load(file.read())


def dump_library(file, catalogue):
    """
    Dumps library into .yaml file.
    :param file: file object.
    :param catalogue: a list of books.
    :returns catalogue in case of success.
    """
    with file:
        yaml.dump(catalogue, file)
        return catalogue
