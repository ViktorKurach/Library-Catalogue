import books
from booksupfunc import book_catalogue
import booksupfunc as bsf

bsf.get_some_tests()

print("Welcome to the Home Library Catalogue(HLC v0.01-alpha)")

while True:
    bsf.print_menu()
    ch = input()
    if ch == '1':
        books.add_book(book_catalogue,bsf.get_book())
    elif ch == '2':
        books.edit_book(book_catalogue,bsf.get_book_name(),bsf.get_author_name(),bsf.get_book())
    elif ch == '3':
        books.delete_book(book_catalogue,bsf.get_book_name(),bsf.get_author_name())
    elif ch == '4':
        year_f, year_t, desc=bsf.get_optional_values()
        bsf.pprint(books.filter_books(book_catalogue,bsf.get_key(),bsf.get_key_value(),year_f,year_t,desc))
    elif ch == '5':
        books.get_authors(book_catalogue,bsf.get_genre())
    elif ch == '0':
        break

