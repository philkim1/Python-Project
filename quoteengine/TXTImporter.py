from typing import List

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TXTImporter(IngestorInterface):
    """This is the TXTImporter class."""
    allowed_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        quote = []

        with open(path, 'r', encoding='utf-8-sig') as file:
            for line in file:
                line = line.strip('\n').strip()
                if len(line) > 0:
                    parse = line.split('-')
                    new = QuoteModel(parse[0], parse[1])
                    quote.append(new)

        return quote
