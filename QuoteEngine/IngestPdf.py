"""Ingestor for files with a .pdf extension."""

import subprocess
import random
import os
from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """Ingests and parses quotes from pdf formatted files.
    
    Must have a .pdf file extension and be correctly formatted for this
    programme. Must have pdftotext installed. 
    
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
            # Create a temporary .txt file
            temp = f'./static/{random.randint(0,100000)}.txt'
            #use pdftotext to read pdf data to the txt file
            subprocess.call(['pdftotext', path, temp])
            with open(temp, 'r') as file:
                for line in file:
                    if line == "\n":
                        break
                    quote_line = line.strip('\n').strip()
                    # print(quote_line[0])
                    if line != "":
                        quote_list = quote_line.split(' - ')
                        quote = QuoteModel(quote_list[0], quote_list[1])
                        quotes.append(quote)
            # Remove the temporary txt file
            os.remove(temp)
            return quotes
        except:
            print('Issue parsing pdf file')
