from meme import get_input, generate_meme
from MemeEngine import MemeEngine
from QuoteEngine import CSVImporter
from QuoteEngine import DocxImporter
from QuoteEngine import PDFImporter


if __name__ == "__main__":
    """Test Importers"""
    # print(PDFImporter.parse('./_data/DogQuotes/DogQuotesPDF.pdf'))
    # print(CSVImporter.parse('./_data/DogQuotes/DogQuotesCSV.csv'))
    # print(DOcxImporter.parse('./_data/DogQuotes/DogQuotesDOCX.docx'))

    """Test making a meme"""
    # meme = MemeEngine('./tmp')
    # img = './_data/photos/dog/xander_1.jpg'
    # body = 'woof woof!'
    # author = 'sparky'
    # path = meme.make_meme(img, body, author)
    # print(path)

    """Generate a user defined meme."""

    args = get_input()

    try:
        print(generate_meme(args.path, args.body, args.author))
    except Exception:
        print('cannot process request')
