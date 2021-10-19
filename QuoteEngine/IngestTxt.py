"""Ingestor for files with a .txt extension."""

from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class TextIngestor(IngestorInterface):
    """Ingests and parses quotes from txt formatted files.
    
    Must have a .txt file extension and be correctly formatted for this
    programme.
    
    Realises the IngestorInterface class.
    """

    extension = ['txt']

    @classmethod    
    def parse(cls, path: str) -> List[QuoteModel]:
        """Test the file extension and return a list of QuoteModels.

        :params: file path that contains the quote data
        :returns: a list of QuoteModels
        """
        if not cls.can_ingest(path):
            file_extension = path.split('.')[-1]
            raise Exception(f'Cannot ingest {file_extension} exception')
        try:
            quotes = []
            with open(path) as file:
                for line in file:
                    if line != "":
                        quote_list = line.split(' - ')
                        quote = QuoteModel(quote_list['0'], quote_list['1'])
                        quotes.append(quote)
            return quotes
        except:
            print('Issue parsing txt file')
