def add_book(catalogue, new):
    """Adds new book to the catalogue. Returns 1 if the book is already in catalogue, or 0 otherwise. Parameter 'new' \
    must be a dictionary with keys: 'path', 'title', 'author', 'publication', 'genre', 'description', 'year'"""
    if new in catalogue:
        return 1
    catalogue.append(new)
    return 0


def search_book(catalogue, title, author):
    """Returns a dictionary corresponding to a book with 'title' written by 'author'. If not found - returns None"""
    for x in catalogue:
        if (x["title"] == title) and (x["author"] == author):
            return x


def edit_book(catalogue, old_title, old_author, new):
    """Replaces a book with a new one. Returns new book in case of success, or None if old book is not found"""
    book = search_book(catalogue, old_title, old_author)
    if book:
        i = catalogue.index(book)
        catalogue.remove(book)
        catalogue.insert(i, new)
        return new


def delete_book(catalogue, title, author):
    """Removes a book from a catalogue. Returns 0 in case of success, or 1 if the book is not found"""
    try:
        catalogue.remove(search_book(catalogue, title, author))
        return 0
    except ValueError:
        return 1


def sort_by_year(book_list, desc):
    """Returns book list sorted by year according to 'desc' parameter (see filter_books description).
    In next versions function will be private: usage outside this module is not recommended"""
    if desc == 1:
        return sorted(book_list, key=lambda x: x["year"])
    if desc == -1:
        return sorted(book_list, key=lambda x: x["year"], reverse=True)
    return book_list


def filter_by_year(book_list, year_from, year_to, desc):
    """Filters books from book list, published between 'year_from' and 'year_to' and sorted according to 'desc' \
    parameter (see filter_books description).
    In next versions function will be private: usage outside this module is not recommended"""
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
    """Filters books by the key and/or publication year. Key must be "author", "genre", or "year". Value is author's \
    or genre's name; if key="year", any value is allowed. If year_from=None, filtering by year is not performed. If \
    year_to=None and not year_from=None, returns only books published in year_from. If desc=1, books are sorted by \
    publish year increasing; if desc=-1, are sorted by year decreasing; otherwise sorting is not performed"""
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
    """Returns a list of authors, whose books relate to genre. If genre=None, returns all authors in the catalogue"""
    authors = []
    for x in catalogue:
        if (x["genre"] == genre) and (x["author"] not in authors):
            authors.append(x["author"])
            continue
        if (genre is None) and (x["author"] not in authors):
            authors.append(x["author"])
    return authors
