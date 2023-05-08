class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def get_book_info(self):
        return f"Title: {self.title}, Author: {self.author}, Price: {self.price}"

def get_total_price(book_list):
    total_price = 0
    for book in book_list:
        book_obj = Book(book["title"], book["author"], book["price"])
        total_price += book_obj.price
    return total_price

description = "this is a module named bookstore"

