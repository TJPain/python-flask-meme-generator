"""IngestorInterface class."""

from abc import ABC, abstractmethod
from typing import List

from QuoteModel import QuoteModel


class IngestorInterface(ABC):    
    """Abstract base class defining two methods.

    This parses a file of various extension types and creates a list of 
    QuoteModel instances
    """

    @classmethod
    def can_ingest(cls, path: str) -> bool:
        """Test file validy for parsing.
        
        Checks if the given file has a valid extension and can therefore
        be parsed.

        :params: file path
        :returns: True if the file has a valid extension and False if it
        does not
        """
        # takes the extension from the strategy object for each file type
        extension = []

        if path.split('.')[-1] in cls.extension:
            return True
        else: 
            return False

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Empty method to be defined by inheriting class."""
        pass
