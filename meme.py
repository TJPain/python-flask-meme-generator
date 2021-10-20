"""meme cli."""

import os
import random
import argparse
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

def generate_meme(path=None, body=None, author=None):
    """Generate a meme given a path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    # Create the parser
    parser = argparse.ArgumentParser(description='Meme generator CLI')
    # Add the arguments
    parser.add_argument('--path',
                        metavar='image path',
                        type=str,
                        default=None,
                        help='the path for an image file')
    parser.add_argument('--body',
                        metavar='quote body',
                        type=str,
                        default=None,
                        help='the body of the quote')
    parser.add_argument('--author',
                        metavar='quote author',
                        type=str,
                        default=None,
                        help='the author of the quote')
    # Execute parse_args()
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
