"""QuoteModel class."""

class QuoteModel():
    """Encapsulate the body of the quote and the author into a new quote model."""

    def __init__(self, body: str, author: str):
        """Create a new quote model.

        :params: the body of the quote and the author of the quote
        """
        self.body = body
        self.author = author

    def __str__(self):
        """Return `str(self)`."""
        return f"Quote: {self.body}" \
               f"Author: {self.author}"

    def __repr__(self):
        """Return `repr(self)."""
        return f"body={self.body}, " \
               f"author={self.author}"