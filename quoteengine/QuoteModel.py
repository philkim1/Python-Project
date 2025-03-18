

class QuoteModel():
    """This is the QuoteModel Class."""

    def __init__(self, body, author):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'({self.body}, {self.author})'
