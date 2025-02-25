
class Book:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def get_info(self):
        return (f'{self.title} - {self.author}')
        pass

    def is_older_than(self, year):
        pass

    def update_year(self, new_year):
        pass

    def set_genre(self, genre):
        pass

    def set_isbn(self, isbn):
        pass

    def get_age(self):
        pass

    def compare_books(self, other_book):
        pass
