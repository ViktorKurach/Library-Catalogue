import io
import unittest
import pickle
import json
import yaml
import books
book_list = [{"path": "Path", "title": "T1", "author": "A1",
              "publication": "P", "genre": "G", "description": "D",
              "year": 1900},
             {"path": "Path", "title": "T2", "author": "A2",
              "publication": "P", "genre": "G", "description": "D",
              "year": 2000},
             {"path": "Path", "title": "T3", "author": "A2",
              "publication": "P", "genre": "G", "description": "D",
              "year": 2010}]


class TestPickle(unittest.TestCase):

    def test_load_library(self):
        file = io.BytesIO(pickle.dumps(book_list))
        books.set_config("config.cfg", "storage", "test_file_type", "pkl")
        self.assertEqual(book_list, books.load_library(file, test_mode=True))

    def test_dump_library(self):
        file = io.BytesIO()
        books.set_config("config.cfg", "storage", "test_file_type", "pkl")
        self.assertEqual(book_list, books.dump_library(file, book_list,
                                                       test_mode=True))


class TestJson(unittest.TestCase):

    def test_load_library(self):
        file = io.StringIO(json.dumps(book_list))
        books.set_config("config.cfg", "storage", "test_file_type", "json")
        self.assertEqual(book_list, books.load_library(file, test_mode=True))

    def test_dump_library(self):
        file = io.StringIO()
        books.set_config("config.cfg", "storage", "test_file_type", "json")
        self.assertEqual(book_list, books.dump_library(file, book_list,
                                                       test_mode=True))


class TestYaml(unittest.TestCase):

    def test_load_library(self):
        file = io.StringIO(yaml.dump(book_list))
        books.set_config("config.cfg", "storage", "test_file_type", "yaml")
        self.assertEqual(book_list, books.load_library(file, test_mode=True))

    def test_dump_library(self):
        file = io.StringIO()
        books.set_config("config.cfg", "storage", "test_file_type", "yaml")
        self.assertEqual(book_list, books.dump_library(file, book_list,
                                                       test_mode=True))


class TestBooks(unittest.TestCase):

    def test_add_book(self):
        catalogue = []
        book = book_list[2]
        self.assertEqual(0, books.add_book(catalogue, book))
        self.assertEqual(1, books.add_book(catalogue, book))

    def test_search_book(self):
        book = book_list[2]
        catalogue = [book]
        self.assertEqual(book, books.search_book(catalogue, "T3", "A2"))
        self.assertEqual(None, books.search_book(catalogue, "TT", "AA"))

    def test_edit_book(self):
        book = book_list[1]
        new = book_list[2]
        catalogue = [book]
        self.assertEqual(new, books.edit_book(catalogue, "T2", "A2", new))
        self.assertEqual(None, books.edit_book(catalogue, "Tit", "A", new))

    def test_delete_book(self):
        book = book_list[2]
        catalogue = [book]
        self.assertEqual(0, books.delete_book(catalogue, "T3", "A2"))
        self.assertEqual(1, books.delete_book(catalogue, "T3", "A2"))

    def test_filter_books(self):
        catalogue = [book_list[1], book_list[0], book_list[2]]
        # Get all of the books:
        self.assertEqual(catalogue,
                         books.filter_books(catalogue, "year", None))
        # Get books, published in only one year, without sorting:
        self.assertEqual([book_list[1]],
                         books.filter_books(catalogue, "year",
                                            "anything", 2000))
        # Get books, published between two years, by year decreasing:
        self.assertEqual([book_list[2], book_list[1]],
                         books.filter_books(catalogue, "year", None,
                                            2000, 2010, -1))
        # Get books, published between two years, by year increasing:
        self.assertEqual([book_list[0], book_list[1], book_list[2]],
                         books.filter_books(catalogue, "year", None,
                                            1900, 2100, 1))
        # Get books of one author from all years, by years decreasing:
        self.assertEqual([book_list[2], book_list[1]],
                         books.filter_books(catalogue, "author", "A2",
                                            None, None, -1))
        # Get books of one author from one year, without sorting:
        self.assertEqual([book_list[1]],
                         books.filter_books(catalogue, "author", "A2", 2000))
        # Get books of one author between two years, by increasing:
        self.assertEqual([book_list[1]],
                         books.filter_books(catalogue, "author", "A2",
                                            2000, 2005, 1))
        # Books of one genre from all years, by years increasing:
        self.assertEqual([book_list[0], book_list[1], book_list[2]],
                         books.filter_books(catalogue, "genre", "G",
                                            None, None, 1))
        # Books of one genre from one year, without sorting:
        self.assertEqual([book_list[1]],
                         books.filter_books(catalogue, "genre", "G", 2000))
        # Books of one genre between two years, by decreasing:
        self.assertEqual([book_list[2], book_list[1]],
                         books.filter_books(catalogue, "genre", "G",
                                            2000, 2015, -1))

    def test_get_authors(self):
        book1 = {"path": "Path", "title": "T1", "author": "A1",
                 "publication": "P", "genre": "G1", "description": "D",
                 "year": 1900}
        book2 = {"path": "Path", "title": "T2", "author": "A2",
                 "publication": "P", "genre": "G1", "description": "D",
                 "year": 2000}
        book3 = {"path": "Path", "title": "T3", "author": "A2",
                 "publication": "P", "genre": "G2", "description": "D",
                 "year": 2010}
        catalogue = [book2, book1, book3]
        self.assertEqual(['A2'], books.get_authors(catalogue, "G2"))
        self.assertEqual(['A2', 'A1'], books.get_authors(catalogue))


if __name__ == '__main__':
    unittest.main()
