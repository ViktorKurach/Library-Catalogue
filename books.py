def add_book(catalogue, new):
    """
    Adds new book to the catalogue. Returns 1 if the book is already in
    catalogue, or 0 otherwise. Parameter 'new' must be a dictionary with keys:
    'path', 'title', 'author', 'publication', 'genre', 'description', 'year'.

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
    Returns a dictionary corresponding to a book. If not found - returns
    nothing.

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
    Replaces a book with a new one. Returns new book in case of success, or
    nothing if old book is not found.

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
    Removes a book from a catalogue. Returns 0 in case of success, or 1 if the
    book is not found.

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
    Returns book list sorted by year according to 'desc' parameter (see
    filter_books description).

    In next versions function will be private: usage outside this module is
    not recommended.

    Function is always called by filter_by_year function: see tests there.
    """
    if desc == 1:
        return sorted(book_list, key=lambda x: x["year"])
    if desc == -1:
        return sorted(book_list, key=lambda x: x["year"], reverse=True)
    return book_list


def filter_by_year(book_list, year_from, year_to, desc):
    """
    Filters books from book list, published between year_from and year_to and
    sorted according to 'desc' parameter (see filter_books description).

    In next versions function will be private: usage outside this module is
    not recommended.

    Function is always called by filter_books function: see tests there.
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
    Filters books by the key and/or publication year. Key must be "author",
    "genre", or "year". Value is author's or genre's name; if key="year", any
    value is allowed.

    If year_from=None, filtering by year is not performed. If year_to=None and
    not year_from=None, returns only books published in year_from.

    If desc=1, books are sorted by publish year increasing; if desc=-1, are
    sorted by year decreasing; otherwise sorting is not performed.

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
    Returns a list of authors, whose books relate to genre. If genre=None,
    returns all authors in the catalogue.

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
