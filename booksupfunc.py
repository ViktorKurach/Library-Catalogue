import books
book_catalogue = []


def get_book():
    """Create new dictionary element by using get_xxx functions;
       :return dictionary element that contains book info"""
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
    """Get book name value;
        :returns standard python function input"""
    print("Title: ")
    return input()


def get_description():
    """Get book description value;
        :returns standard python function input"""
    print("Description:")
    return input()


def get_path():
    """Get book path value;
        :returns standard python function input"""
    print("Path: ")
    return input()


def get_publication():
    """Get book publication value;
        :returns standard python function input"""
    print("Publication: ")
    return input()


def get_author_name():
    """Get book author name value;
        :returns standard python function input"""
    print("Author: ")
    return input()


def get_year():
    """Get book year value;
        :returns: None: if year value cannot be converted
                    OR integer value of year"""
    print("Year: ")
    year = input()
    try:
        year = int(year)
    except ValueError:
        return None
    return year


def get_key():
    """Get key name for filtering function;\
        :returns standard python function input"""
    print("Filter key(author,genre or year): ")
    return input()


def get_key_value():
    """Get filter key value value;
        :returns standard python function input"""
    print("Enter key value: ")
    return input()


def get_optional_values():
    """Get optional values for filtering function;
        if input value of sort order cannot be converted to int turns desc to 0
        else sort order is converted value
        :returns: year_f,year_t: integer values of years
                  desc: sort order"""
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
    """Get genre name

    :returns: None: if genre is not containing
                any symbol or containing only whitespaces
              OR genre name if genre was inputted """
    print("Genre: ")
    _genre = input()
    if _genre == '' or _genre.isspace():
        _genre = None
    return _genre


def mod_chosen():
    """
    Choose format of library file
    :returns: 'w' if chosen formats are json or yaml
                or 'wb' if chosen format is pickle
    """
    print('\n Choose format of library(pickle, json, yaml):')
    ch = input()
    if ch == 'json' or ch == 'yaml':
        return 'w'
    elif ch == 'pickle':
        return 'wb'


def load_library():
    """Load books from inputted library file
    :return: function load_library from  books module
    """
    print('\n Enter name of library file:')
    file_name = input()
    file = open(file_name, 'rb')
    return books.load_library(file)


def dump_into_library():
    """Dump current book catalogue into inputted library file"""
    print('\n Enter name of library file:')
    file_name = input()
    file = open(file_name, mod_chosen())
    books.dump_library(file, book_catalogue)


def print_menu():
    """Print simple console menu"""
    print("\nMenu:\n")
    print("1. Add book to the catalogue\n")
    print("2. Edit book in the catalogue\n")
    print("3. Delete book from the catalogue\n")
    print("4. Filter books\n")
    print("5. Get authors\n")
    print("6. Load catalogue from library\n")
    print("7. Dump catalogue into library\n")
    print("0. Finish work")


def pprint(catalogue):
    """Prints values of all elements in book catalogue
    :param catalogue: a list of books.
    """
    for i in catalogue:
        print("\nPath: {}, Title: {}".format(i['path'], i['title']))
        print("Author: {}".format(i['author']))
        print("Genre: {}, Year: {}".format(i['genre'], i['year']))
        print("Description: {}\n".format(i['description']))


def print_authors(authors):
    """Prints names of all authors
    :param: authors: a list of authors"""
    for i in authors:
        print("Author: {}".format(i))
