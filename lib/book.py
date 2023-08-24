
class Book:
    pass
class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count

    

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

class TestBookMethods():
    def test_requires_int_page_count(self):
        '''prints "page_count must be an integer" if page_count is not an integer.'''
        book = Book("And Then There Were None", 272)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.page_count = "not an integer"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "page_count must be an integer\n"

    def test_turn_page(self):
        '''tests turning pages'''
        book = Book("Sample Book", 5)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        book.turn_page()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_out.getvalue(), "Flipping the page...wow, you read fast!\n")

if __name__ == '__main__':
    unittest.main()







