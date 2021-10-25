"""Ingestor selects the appropriate ingestor helper function.

Ingestor realizes IngestorInterface and encapsulates ingestor
helper classes. Logic is used to select the appropriate helper.
"""
from typing import List

from .IngestCsv import CSVIngestor
from .IngestDocx import DocxIngestor
from .IngestPdf import PDFIngestor
from .IngestTxt import TextIngestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class Ingestor(IngestorInterface):
    """Encapsulates and calls Ingestor helper classes.
    
    Realises the IngestorInterface class.
    """

    def parse(path: str) -> List[QuoteModel]:
        """Test the file extension and return a list of QuoteModels.

        :params: file path that contains the quote data
        :returns: calls the relevant ingestor helper class for the file type
        """
        ingestors = {
            'csv': CSVIngestor,
            'docx': DocxIngestor,
            'pdf': PDFIngestor,
            'txt': TextIngestor
        }
        file_extension = path.split('.')[-1]

        try:
            for ingestor in ingestors.items():
                if ingestor[0] == file_extension:
                    return ingestor[1].parse(path)
        except:
            print('Issue selecting Ingestor helper')
