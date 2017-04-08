import books
book_catalogue = []


def get_book():
    """Create new dictionary element by using get_xxx functions;
     return dictionary"""
    buf = {}
    print("\nEnter new book\n")
    buf['path'] = get_path()
    buf['title'] = get_book_name()
    buf['author'] = get_author_name()
    buf['publication'] = get_publication()
    buf['genre'] = get_genre()
    buf['description'] = get_description()
    buf['year'] = get_year()
    return buf


def get_book_name():
    """Using to get book name value;
        returns standard python function input"""
    print("Title: ")
    return input()


def get_description():
    """Using to get book description value;
        returns standard python function input"""
    print("Description:")
    return input()


def get_path():
    """Using to get book path value;
        returns standard python function input"""
    print("Path: ")
    return input()


def get_publication():
    """Using to get book publication value;
        returns standard python function input"""
    print("Publication: ")
    return input()


def get_author_name():
    """Using to get book author name value;
        returns standard python function input"""
    print("Author: ")
    return input()


def get_year():
    """Using to get book year value;
        if year value cannot be converted returns None
        else return integer value of year"""
    print("Year: ")
    year = input()
    try:
        year = int(year)
    except ValueError:
        return None
    return year


def get_key():
    """Using to get key name for filtering function;\
        return standard python function input"""
    print("Filter key(author,genre or year): ")
    return input()


def get_key_value():
    """Using to get filter key value value;
        returns standard python function input"""
    print("Enter key value: ")
    return input()


def get_optional_values():
    """Using to get optional values for filtering function;
        uses get_year function to get years;
        if input value of sort order cannot be converted to int returns 0
        else sort order is converted value
        return integer values of years and sort order"""
    print("From(optional) ")
    year_f = get_year()
    print("To(optional) ")
    year_t = get_year()
    print("Sort(optional) : 1 - ascending, -1 - descending")
    try:
        desc = int(input())
    except ValueError:
        desc = 0
    return year_f, year_t, desc


def get_genre():
    """Using to get genre value; if genre is not containing
    any symbol or containing only whitespaces return None"""
    print("Genre: ")
    _genre = input()
    if _genre == '' or _genre.isspace():
        _genre = None
    return _genre


def print_menu():
    """Using to print menu"""
    print("\nMenu:\n")
    print("1. Add book to the catalogue\n")
    print("2. Edit book in the catalogue\n")
    print("3. Delete book from the catalogue\n")
    print("4. Filter books\n")
    print("5. Get authors\n")
    print("0. Finish work")


def pprint(catalogue):
    """Using to print values of all elements in book catalogue that came"""
    for i in catalogue:
        print("\nPath: {}, Title: {}".format(i['path'], i['title']))
        print("Author: {}".format(i['author']))
        print("Genre: {}, Year: {}".format(i['genre'], i['year']))
        print("Description: {}\n".format(i['description']))


def print_authors(authors):
    """Using to print all elements of list of authors"""
    for i in authors:
        print("Author: {}".format(i))


def get_some_tests():
    """Using to put some sample books into database;
    adds dictionaries that contain books info database using add_book function
    """
    book1 = {"path": "C:\\Books", "title": "Перехресні стежки",
             "author": "Іван Франко", "publication": "Фоліо",
             "genre": "Пригодницький роман",
             "description": "Мясо, матюки, убийства", "year": 1686}
    book2 = {"path": "C:\\Books", "title": "Ворошиловград",
             "author": "Сергій Жадан",
             "publication": "Клуб сімейного дозвілля",
             "genre": "Роман",
             "description": "Мясо, матюки, убийства", "year": 2010}
    book3 = {"path": "C:\\Books", "title": "Месопотамія",
             "author": "Сергій Жадан",
             "publication": "Клуб сімейного дозвілля", "genre": "Поезія",
             "description": "Урбаністична збірка про Харків",
             "year": 2014}
    book4 = {"path": "C:\\Books", "title": "Колекціонер",
             "author": "Джон Фаулз",
             "publication": "Клуб сімейного дозвілля", "genre": "Роман",
             "description": "Книга про поїхавшого", "year": 2016}
    books.add_book(book_catalogue, book4)
    books.add_book(book_catalogue, book3)
    books.add_book(book_catalogue, book2)
    books.add_book(book_catalogue, book1)
