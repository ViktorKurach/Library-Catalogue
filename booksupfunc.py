import books
book_catalogue = []


def get_book():
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
    print("Title: ")
    return input()


def get_description():
    print("Description:")
    return input()


def get_path():
    print("Path: ")
    return input()


def get_publication():
    print("Publication: ")
    return input()


def get_author_name():
    print("Author: ")
    return input()


def get_year():
    print("Year: ")
    year = input()
    try:
        year = int(year)
    except ValueError:
        return None
    return year


def get_key():
    print("Filter key: \n")
    return input()


def get_key_value():
    print("Enter key value: ")
    return input()


def get_optional_values():
    print("From(optional): ")
    year_f = get_year()
    print("To(optional): ")
    year_t = get_year()
    print("Sort(optional) : 1 - ascending, -1 - descending")
    try:
        desc = int(input())
    except ValueError:
        desc=0
    return year_f,year_t,desc


def get_genre():
    print("Genre: ")
    _genre=input()
    if _genre == '' or _genre.isspace():
        _genre = None
    return _genre


def print_menu():
    print("\nMenu:\n")
    print("1. Add book to the catalogue\n")
    print("2. Edit book in the catalogue\n")
    print("3. Delete book from the catalogue\n")
    print("4. Filter books\n")
    print("5. Get authors\n")
    print("0. Finish work")


def get_some_tests():
    book1 = {"path": "C:\\Books", "title": "Перехресні стежки", "author": "Іван Франко", "publication": "Фоліо",
             "genre": "Пригодницький роман", "description": "Мясо, матюки, убийства", "year": 1686}
    book2 = {"path": "C:\\Books", "title": "Ворошиловград", "author": "Сергій Жадан",
             "publication": "Клуб сімейного дозвілля", "genre": "Роман", "description": "Мясо, матюки, убийства",
             "year": 2010}
    book3 = {"path": "C:\\Books", "title": "Месопотамія", "author": "Сергій Жадан",
             "publication": "Клуб сімейного дозвілля", "genre": "Поезія",
             "description": "Урбаністична збірка про Харків",
             "year": 2014}
    book4 = {"path": "C:\\Books", "title": "Колекціонер", "author": "Джон Фаулз",
             "publication": "Клуб сімейного дозвілля", "genre": "Роман", "description": "Книга про поїхавшого",
             "year": 2016}
    books.add_book(book_catalogue, book4)
    books.add_book(book_catalogue, book3)
    books.add_book(book_catalogue, book2)
    books.add_book(book_catalogue, book1)