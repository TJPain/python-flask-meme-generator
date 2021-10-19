"""Ingestor for files with a .docx extension."""

from docx import Document
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DocxIngestor(IngestorInterface):
    """Ingests and parses quotes from docx formatted files.
    
    Must have a .docx file extension and be correctly formatted for this
    programme. Docx must also be installed.
    
    Realises the IngestorInterface class.
    """

    extension = ['docx']

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
            doc = Document(path)
            for paragraph in doc.paragraphs:
                if paragraph.text != "":
                    quote_list = paragraph.text.split(' - ')
                    quote = QuoteModel(quote_list['0'], quote_list['1'])
                    quotes.append(quote)
            return quotes
        except:
            print('Issue parsing docx file')
