"""Ingestor for files with a .csv extension."""

import pandas
from typing import List

from .IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """Ingests and parses quotes from csv formatted files.
    
    Must have a .csv file extension and be correctly formatted for this
    programme. Pandas must also be installed.
    
    Realises the IngestorInterface class.
    """

    extension = ['csv']

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
            reader = pandas.read_csv(path, header = 0)
            for index, row in reader.iterrows():
                quote = QuoteModel(row['body'], row['author'])
                quotes.append(quote)
            return quotes
        except:
            print('Issue parsing csv file')
