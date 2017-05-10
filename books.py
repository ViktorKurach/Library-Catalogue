def add_book(catalogue, new):
    """
    Adds new book to the catalogue.
    :param catalogue: a list of books, which new book is added to.
    :param new: a dictionary with next keys: 'path', 'title', 'author',
    'publication', 'genre', 'description', 'year'.
    :returns 1 if the book is already in catalogue, or 0 otherwise.
    """
    if new in catalogue:
        return 1
    catalogue.append(new)
    return 0


def search_book(catalogue, title, author):
    """
    Searches a book in the catalogue.
    :param catalogue: a list of books, which the search is performed in.
    :param title: a string - title of the book, which is searched.
    :param author: a string - name of author of the book, which is searched.
    :returns a dictionary, corresponding to searched book, or nothing, if book
    is not found.
    """
    for x in catalogue:
        if (x["title"] == title) and (x["author"] == author):
            return x


def edit_book(catalogue, old_title, old_author, new):
    """
    Edits a book in the catalogue.
    :param catalogue: a list of books.
    :param old_title: a string - title of the book, which will be edited.
    :param old_author: a string - author of the book, which will be edited.
    :param new: a dictionary, containing new information about the book;
    must have keys: 'path', 'title', 'author', 'publication', 'genre',
    'description', 'year'.
    :returns new book in case of success, or nothing, if old book is not
    found in the catalogue.
    """
    book = search_book(catalogue, old_title, old_author)
    if book:
        i = catalogue.index(book)
        catalogue.remove(book)
        catalogue.insert(i, new)
        return new


def delete_book(catalogue, title, author):
    """
    Removes a book from the catalogue.
    :param catalogue: a list of books.
    :param title: a string - title of the book, which will be deleted.
    :param author: a string - author of the book, which will be deleted.
    :returns 0 in case of success, or 1, if the book is not found in catalogue.
    """
    try:
        catalogue.remove(search_book(catalogue, title, author))
        return 0
    except ValueError:
        return 1


def sort_by_year(book_list, desc):
    """
    Sorts a list of books by publishing year.
    :param book_list: a list of books, that is sorted.
    :param desc: if 1, sorts books by publishing year increasing, if -1 - by
    publishing year decreasing; otherwise sorting is not performed.
    :returns a sorted list of books.

    In next versions function will be private: usage outside this module is
    not recommended.
    """
    if desc == 1:
        return sorted(book_list, key=lambda x: x["year"])
    if desc == -1:
        return sorted(book_list, key=lambda x: x["year"], reverse=True)
    return book_list


def filter_by_year(book_list, year_from, year_to, desc):
    """
    Filters books by publishing year and/or sorts them.
    :param book_list: a list of books, that is filtered.
    :param year_from: an integer, lower limit of publishing years' diapason;
    if year_from=None, filtering is not performed.
    :param year_to: an integer, higher limit of publishing year's diapason;
    if year_to=None and year_from is not None, searches only books, published
    in year_from; if year_from=None, any year_to is allowed.
    :param desc: if 1, sorts selected books by publishing year increasing,
    if -1 - by publishing year decreasing; otherwise sorting is not performed.
    :returns a filtered and sorted list of books.

    In next versions function will be private: usage outside this module is
    not recommended.
    """
    if year_from is None:
        return sort_by_year(book_list, desc)
    if year_to is None:
        year_to = year_from
    res = []
    for x in book_list:
        if (x["year"] in range(year_from, year_to+1)) and (x not in res):
            res.append(x)
    return sort_by_year(res, desc)


def filter_books(catalogue, key, value, year_from=None, year_to=None, desc=0):
    """
    Filters books by the key and/or publishing year and sorts them.
    :param catalogue: a list of books, that is filtered.
    :param key: "genre", "author", or "year".
    :param value: a string, genre's name, if key="genre"; a string, author's
    name, if key="author"; if key="year", any value is allowed.
    :param year_from: an integer, lower limit of publishing years' diapason;
    if year_from=None, filtering by year is not performed.
    :param year_to: an integer, higher limit of publishing year's diapason;
    if year_to=None and year_from is not None, searches only books, published
    in year_from; if year_from=None, any year_to is allowed.
    :param desc: if 1, sorts selected books by publishing year increasing,
    if -1 - by publishing year decreasing; otherwise sorting is not performed.
    :returns a filtered and sorted list of books.
    """
    if key not in ["author", "genre", "year"]:
        return
    if key == "year":
        return filter_by_year(catalogue, year_from, year_to, desc)
    res = []
    for x in catalogue:
        if (x[key] == value) and (x not in res):
            res.append(x)
    return filter_by_year(res, year_from, year_to, desc)


def get_authors(catalogue, genre=None):
    """
    Selects authors, whose books relate to genre.
    :param catalogue: a list of books.
    :param genre: a string - name of the genre, authors must relate to;
    if None, returns all of the authors in catalogue.
    :returns list of strings - authors' names.
    """
    authors = []
    for x in catalogue:
        if (x["genre"] == genre) and (x["author"] not in authors):
            authors.append(x["author"])
            continue
        if (genre is None) and (x["author"] not in authors):
            authors.append(x["author"])
    return authors


def get_config(filename, section, option):
    """
    Parses .cfg file and gets some value from it.
    :param filename: a string - file name.
    :param section: a string - name of section.
    :param option: a string - name of option.
    :returns value of option in section in case of success, or nothing
    otherwise.
    """
    import configparser
    config = configparser.RawConfigParser()
    config.read(filename)
    return config.get(section, option)


def set_config(filename, section, option, new_value):
    """
    Parses .cfg file and sets new value for some option.
    :param filename: a string - file name.
    :param section: a string - name of section.
    :param option: a string - name of option.
    :param new_value: a new value of option in section.
    :returns new_value in case of success, or nothing otherwise.
    """
    import configparser
    config = configparser.RawConfigParser()
    config.read(filename)
    config.set(section, option, new_value)
    with open(filename, "w") as configfile:
        config.write(configfile)
    return new_value


def import_db_module(file_type):
    """
    Imports and returns one of db_xxx modules depending on file_type.
    :param file_type: "pkl", "json" or "yaml"
    :return: if file_type="pkl", returns module db_pickle; if file_type="json",
    returns module db_json; if file_type="yaml", returns module db_yaml.

    In next versions function will be private: usage outside this module is not
    recommended.
    """
    if file_type == "pkl":
        import db_pickle
        return db_pickle
    elif file_type == "json":
        import db_json
        return db_json
    elif file_type == "yaml":
        import db_yaml
        return db_yaml


def load_library(file, test_mode=False):
    """
    Loads a book list from .pkl, .json or .yaml file.
    :param file: a file object; file must be opened in "rb" mode, and be the
    same type, as set in 'db_file_type' option in 'config.cfg'. Otherwise
    function's work is unpredictable.
    :param test_mode: if True, 'test_file_type' option instead of
    'db_file_type' is used.
    :returns loaded list of books in case of success.
    """
    if test_mode:
        file_type = get_config("config.cfg", "storage", "test_file_type")
    else:
        file_type = get_config("config.cfg", "storage", "db_file_type")
    db = import_db_module(file_type)
    return db.load_library(file)


def dump_library(file, catalogue, test_mode=False):
    """
    Dumps list of books into .pkl, .json or .yaml file.
    :param file: a file object; file must be opened in "wb" mode, if it is
    .pkl, or in "w" mode if it is .json or .yaml; file type must be the same,
    as set in 'db_file_type' option in 'config.cfg'. Otherwise function's work
    is unpredictable.
    :param catalogue: a list of books.
    :param test_mode: if True, 'test_file_type' option instead of
    'db_file_type' is used.
    :returns catalogue in case of success.
    """
    if test_mode:
        file_type = get_config("config.cfg", "storage", "test_file_type")
    else:
        file_type = get_config("config.cfg", "storage", "db_file_type")
    db = import_db_module(file_type)
    return db.dump_library(file, catalogue)
