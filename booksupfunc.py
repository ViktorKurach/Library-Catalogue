import books
book_catalogue=[]


class Support:
    """
    A class working with library directly.
    Contents methods:
    1. __init__(self)
    2. add_book(self, new)
    3. search_book(self, title, author)
    4. edit_book(self, old_title, old_author, new)
    5. delete_book(self, title, author)
    6. filter_books(self, key, value, year_from=None, year_to=None, desc=0)
    7. get_authors(self, genre=None)
    8. get_config(filename, section, option)
    9. set_config(filename, section, option, new_value)
    10. load_library(self, file, test_mode=False)
    11. dump_library(self, file)
    """
    catalogue = books.Library()
    def __init__(self):
        """"""
        #catalogue = books.Library()

    def get_book(self):
        """Create new dictionary element by using get_xxx functions;
       :return dictionary element that contains book info"""
        buf = {}
        print("\nEnter new book\n")
        buf['path'] = input("Path: ")
        buf['title'] = input("Title: ")
        buf['author'] = input("Author: ")
        buf['publication'] = input("Publication: ")
        buf['genre'] = self.get_genre(self)
        buf['description'] = input("Description: ")
        buf['year'] = self.get_year(self)
        return buf

    @staticmethod
    def get_year(self):
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

    @staticmethod
    def get_key(self):
        """Get key name for filtering function;\
        :returns standard python function input"""
        print("Filter key(author,genre or year): ")
        return input()

    @staticmethod
    def get_key_value(self):
        """Get filter key value value;
        :returns standard python function input"""
        print("Enter key value: ")
        return input()

    @staticmethod
    def get_optional_values(self):
        """Get optional values for filtering function;
        if input value of sort order cannot be converted to int turns desc to 0
        else sort order is converted value
        :returns: year_f,year_t: integer values of years
                  desc: sort order"""
        print("From(optional) ")
        year_f = self.get_year()
        print("To(optional) ")
        year_t = self.get_year()
        print("Sort(optional) : 1 - ascending, -1 - descending")
        try:
            desc = int(input())
        except ValueError:
            desc = 0
        return year_f, year_t, desc

    @staticmethod
    def get_genre(self):
        """Get genre name

        :returns: None: if genre is not containing
                any symbol or containing only whitespaces
              OR genre name if genre was inputted """
        print("Genre: ")
        _genre = input()
        if _genre == '' or _genre.isspace():
            _genre = None
        return _genre

    @staticmethod
    def mod_chosen(self):
        """
        Choose format of library file
        :returns: 'w' if chosen formats are json or yaml
                or 'wb' if chosen format is pickle
        """
        print('\n Choose format of library(pickle, json, yaml):')
        ch=input()
        if ch == 'json' or ch == 'yaml':
            return 'w'
        elif ch == 'pickle':
            return 'wb'

    @staticmethod
    def load_library(self):
        """Load books from inputted library file
        :return: function load_library from  books module
        """
        print('\n Enter name of library file:')
        file_name = input()
        file=open(file_name, 'rb')
        return self.catalogue.load_library(file)

    @staticmethod
    def dump_into_library(self):
        """Dump current book catalogue into inputted library file"""
        print('\n Enter name of library file:')
        file_name = input()
        try:
            file = open(file_name, self.mod_chosen())
            self.catalogue.dump_library(file,book_catalogue)
        except:
            print("Can`t open file: {:}".format(file_name))

    @staticmethod
    def print_menu(self):
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

    @staticmethod
    def pprint(self, catalogue):
        """Prints values of all elements in book catalogue
        :param catalogue: a list of books.
        """
        for i in catalogue:
            print("\nPath: {}, Title: {}".format(i['path'], i['title']))
            print("Author: {}".format(i['author']))
            print("Genre: {}, Year: {}".format(i['genre'], i['year']))
            print("Description: {}\n".format(i['description']))

    @staticmethod
    def print_authors(self, authors):
        """Prints names of all authors
        :param: authors: a list of authors"""
        for i in authors:
            print("Author: {}".format(i))

    def menu(self):
        """d"""
        while True:
            self.print_menu(self)
            ch = input()
            if ch == '1':
                self.catalogue.add_book(self.get_book())
            elif ch == '2':
                self.catalogue.edit_book(input("Title: "),
                                         input("Author: "), self.get_book())
            elif ch == '3':
                self.catalogue.delete_book(input("Title: "),
                                           input("Author: "))
            elif ch == '4':
                year_f, year_t, desc = self.get_optional_values(self)
                self.pprint(self,self.catalogue.filter_books(self.get_key(self),
                                               self.get_key_value(self), year_f, year_t,
                                              desc))
            elif ch == '5':
                self.print_authors(self, self.catalogue.get_authors(self.get_genre(self)))
            elif ch == '6':
                self.load_library(self)
            elif ch == '7':
                self.dump_into_library(self)
            elif ch == '0':
                break
