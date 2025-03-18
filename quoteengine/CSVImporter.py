from typing import List
import pandas

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVImporter(IngestorInterface):
    """This is the CSVImporter class."""
    allowed_extensions = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of quotes and authors."""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        quote = []
        df = pandas.read_csv(path, header=0)

        for index, row in df.iterrows():
            new = QuoteModel(row['body'], row['author'])
            quote.append(new)

        return quote
