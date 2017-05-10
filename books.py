def add_book(catalogue, new):
    """
    Adds new book to the catalogue.
    :param catalogue: a list of books, which new book is added to.
    :param new: a dictionary with next keys: 'path', 'title', 'author',
    'publication', 'genre', 'description', 'year'.
    :returns 1 if the book is already in catalogue, or 0 otherwise.

    >>> catalogue = []
    >>> book = {"path": "Path", "title": "T", "author": "A",\
    "publication": "P", "genre": "G", "description": "D", "year": 2017}
    >>> add_book(catalogue, book)
    0
    >>> add_book(catalogue, book)
    1
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

    >>> book = {"path": "Path", "title": "T", "author": "A",\
    "publication": "P", "genre": "G", "description": "D", "year": 2017}
    >>> catalogue = [book]
    >>> search_book(catalogue, "T", "A")
    {'path': 'Path', 'title': 'T', 'author': 'A', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2017}
    >>> search_book(catalogue, "TT", "AA")
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

    >>> book = {"path": "Path", "title": "TT", "author": "AA",\
    "publication": "P", "genre": "G", "description": "D", "year": 1800}
    >>> new = {"path": "Path", "title": "T", "author": "A",\
    "publication": "P", "genre": "G", "description": "D", "year": 2017}
    >>> catalogue = [book]
    >>> edit_book(catalogue, "TT", "AA", new)
    {'path': 'Path', 'title': 'T', 'author': 'A', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2017}
    >>> edit_book(catalogue, "Tit", "A", new)
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

    >>> book = {"path": "Path", "title": "T", "author": "A",\
    "publication": "P", "genre": "G", "description": "D", "year": 2017}
    >>> catalogue = [book]
    >>> delete_book(catalogue, "T", "A")
    0
    >>> delete_book(catalogue, "T", "A")
    1
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

    Function is always called by filter_by_year(): see tests there.
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

    Function is always called by filter_books(): see tests there.
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

    >>> book1 = {"path": "Path", "title": "T1", "author": "A1",\
    "publication": "P", "genre": "G", "description": "D", "year": 1900}
    >>> book2 = {"path": "Path", "title": "T2", "author": "A2",\
    "publication": "P", "genre": "G", "description": "D", "year": 2000}
    >>> book3 = {"path": "Path", "title": "T3", "author": "A2",\
    "publication": "P", "genre": "G", "description": "D", "year": 2010}
    >>> catalogue = [book2, book1, book3]

    All of the books:
    >>> filter_books(catalogue, "year", None)
    [{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}, \
{'path': 'Path', 'title': 'T1', 'author': 'A1', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 1900}, \
{'path': 'Path', 'title': 'T3', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2010}]

    Books published in only one year, without sorting:
    >>> filter_books(catalogue, "year", "anything", 2000)
    [{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}]

    Books published between two years, by year decreasing:
    >>> filter_books(catalogue, "year", None, 2000, 2010, -1)
    [{'path': 'Path', 'title': 'T3', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2010}, \
{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}]

    Books published between two years, by year increasing:
    >>> filter_books(catalogue, "year", None, 1900, 2100, 1)
    [{'path': 'Path', 'title': 'T1', 'author': 'A1', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 1900}, \
{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}, \
{'path': 'Path', 'title': 'T3', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2010}]

    Books of one author from all years, by years decreasing:
    >>> filter_books(catalogue, "author", "A2", None, None, -1)
    [{'path': 'Path', 'title': 'T3', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2010}, \
{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}]

    Books of one author from one year, without sorting:
    >>> filter_books(catalogue, "author", "A2", 2000)
    [{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}]

    Books of one author between two years, by increasing:
    >>> filter_books(catalogue, "author", "A2", 2000, 2005, 1)
    [{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}]

    Books of one genre from all years, by years increasing:
    >>> filter_books(catalogue, "genre", "G", None, None, 1)
    [{'path': 'Path', 'title': 'T1', 'author': 'A1', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 1900}, \
{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}, \
{'path': 'Path', 'title': 'T3', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2010}]

    Books of one genre from one year, without sorting:
    >>> filter_books(catalogue, "genre", "G", 2000)
    [{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}]

    Books of one genre between two years, by decreasing:
    >>> filter_books(catalogue, "genre", "G", 2000, 2015, -1)
    [{'path': 'Path', 'title': 'T3', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2010}, \
{'path': 'Path', 'title': 'T2', 'author': 'A2', 'publication': 'P', \
'genre': 'G', 'description': 'D', 'year': 2000}]
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

    >>> book1 = {"path": "Path", "title": "T1", "author": "A1",\
    "publication": "P", "genre": "G1", "description": "D", "year": 1900}
    >>> book2 = {"path": "Path", "title": "T2", "author": "A2",\
    "publication": "P", "genre": "G1", "description": "D", "year": 2000}
    >>> book3 = {"path": "Path", "title": "T3", "author": "A2",\
    "publication": "P", "genre": "G2", "description": "D", "year": 2010}
    >>> catalogue = [book2, book1, book3]
    >>> get_authors(catalogue, "G2")
    ['A2']
    >>> get_authors(catalogue)
    ['A2', 'A1']
    """
    authors = []
    for x in catalogue:
        if (x["genre"] == genre) and (x["author"] not in authors):
            authors.append(x["author"])
            continue
        if (genre is None) and (x["author"] not in authors):
            authors.append(x["author"])
    return authors


if __name__ == "__main__":
    import doctest
    doctest.testmod()
