class BookDAO:
    def get_all_books(self):
        books = Book.query.all()
        return