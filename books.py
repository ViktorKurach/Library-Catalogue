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
    """Returns book list sorted by year. If desc=1, sorts by increase; if desc=-1, sorts by decrease; otherwise \
    sorting is not performed"""
    if desc == 1:
        return sorted(book_list, key=lambda x: x["year"])
    elif desc == -1:
        return sorted(book_list, key=lambda d: d["year"], reverse=True)
    return book_list


def filter_books(catalogue, key, value, year_from=None, year_to=None, desc=0):
    """Filters books by the key and/or publication year. Key must be "author", "genre", or "year". Value is author's \
    or genre's name; if key="year", any value is allowed. If year_from=None, filtering by year is not performed. If \
    year_to=None, returns only books published in year_from. If desc=1, books are sorted by publish date increasing; \
    if desc=-1, are sorted by date decreasing; otherwise sorting is not performed"""
    if key not in ["author", "genre", "year"]:
        return
    buf, res = [], []
    if key == "year":
        buf = catalogue
    else:
        for x in catalogue:
            if (x[key] == value) and (x not in buf):
                buf.append(x)
    if year_to is None:
        year_to = year_from
    if year_from is not None:
        for x in buf:
            if (x["year"] in range(year_from, year_to+1)) and (x not in res):
                res.append(x)
    else:
        res = buf
    return sort_by_year(res, desc)


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


# Tests
books = []
book1 = {"path": "C:\\Books", "title": "Перехресні стежки", "author": "Іван Франко", "publication": "Фоліо",
         "genre": "Пригодницький роман", "description": "Мясо, матюки, убийства", "year": 1686}
book2 = {"path": "C:\\Books", "title": "Ворошиловград", "author": "Сергій Жадан",
         "publication": "Клуб сімейного дозвілля", "genre": "Роман", "description": "Мясо, матюки, убийства",
         "year": 2010}
book3 = {"path": "C:\\Books", "title": "Месопотамія", "author": "Сергій Жадан",
         "publication": "Клуб сімейного дозвілля", "genre": "Поезія", "description": "Урбаністична збірка про Харків",
         "year": 2014}
book4 = {"path": "C:\\Books", "title": "Колекціонер", "author": "Джон Фаулз",
         "publication": "Клуб сімейного дозвілля", "genre": "Роман", "description": "Книга про поїхавшого",
         "year": 2016}
add_book(books, book2)
add_book(books, book3)
add_book(books, book1)
print(books)
print(add_book(books, book1))
print(add_book(books, book4))
print(search_book(books, "Бійцівський клуб", "Чак Поланік"))
print(search_book(books, "Колекціонер", "Джон Фаулз"))
new_book = {"path": "C:\\Books", "title": "Перехресні стежки", "author": "Іван Франко", "publication": "Фоліо",
            "genre": "Повість", "description": "Класика укр. літ.", "year": 1900}
edit_book(books, "Бійцівський клуб", "Чак Поланик", new_book)
edit_book(books, "Перехресні стежки", "Іван Франко", new_book)
print(delete_book(books, "Колекціонер", "Джон Фаулз"))
print(delete_book(books, "Бійцівський клуб", "Чак Поланік"))
print(filter_books(books, "year", "anything", None, None, -1))
print(filter_books(books, "year", None, 2010))
print(filter_books(books, "year", 228, 2005, 2017))
print(filter_books(books, "author", "Сергій Жадан", None, None, -1))
print(filter_books(books, "author", "Іван Франко", 1900))
print(filter_books(books, "author", "Сергій Жадан", 2007, 2012))
print(filter_books(books, "genre", "Повість", None, 2114, 1))
print(filter_books(books, "genre", "Повість", 1900))
print(filter_books(books, "genre", "Поезія", 1800, 2050, 1))
print(get_authors(books))
print(get_authors(books, "Роман"))
print(get_authors(books, "Детектив"))
print(books)
