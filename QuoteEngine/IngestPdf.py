"""Ingestor for files with a .pdf extension."""

import subprocess
from typing import List

from .IngestorInterface import IngestorInterface
from QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """Ingests and parses quotes from pdf formatted files.
    
    Must have a .pdf file extension and be correctly formatted for this
    programme.
    
    Realises the IngestorInterface class.
    """

    extension = ['pdf']

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
            # doc = Document(path)
            # for paragraph in doc.paragraphs:
            #     if paragraph.text != "":
            #         quote_list = paragraph.text.split(' - ')
            #         quote = QuoteModel(quote_list['0'], quote_list['1'])
            #         quotes.append(quote)
            return quotes
        except:
            print('Issue parsing pdf file')
