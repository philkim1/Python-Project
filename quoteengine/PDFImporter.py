from typing import List
import subprocess
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFImporter(IngestorInterface):
    """This is the PDFImporter class."""
    allowed_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of quotes and authors"""
        if not cls.can_ingest(path):
            raise Exception('cannot ingest')

        tmp = f'./tmp/{random.randint(0, 999999)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])
        file_ref = open(tmp, 'r')
        quote = []

        for line in file_ref.readlines():
            line = line.strip('\n\r').strip()
            if len(line) > 0:
                parse = line.split('-')
                new = QuoteModel(parse[0], parse[1])
                quote.append(new)

        file_ref.close()
        os.remove(tmp)
        return quote
