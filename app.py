"""Meme flask application."""

import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    # iterate through files and add quotes to quotes variable
    try:
        for file in quote_files:
            quotes.extend(Ingestor.parse(file))
    except: 
        print('Error iterating through and ingesting quote files')

    images_path = "./_data/photos/dog/"

    # find all images within the images images_path directory
    imgs = None

    try: 
        for root, dirs, files in os.walk(images_path, topdown=True):
            for file in files:
                imgs.append(os.path.join(root, file))
    except: 
        print(f'Error walking image path: {images_path}') 
    
    return quotes, imgs

quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """Generate a random meme."""
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    #temporary path
    tmp_file = f'./static/{random.randint(0, 1000000)}.jpg'
    
    #user params
    img_url = request.form.get('image_url')
    body = request.form.get('body', '')
    author = request.form.get('author', '')
    
    #save the image as a temporary local file
    try:
        image_content = requests.get(img_url, stream=True).content
        with open(tmp_file, 'wb') as img:
            img.write(image_content)
    except: 
        print('Error saving the image as a temporary file')

    #create the meme
    try:
        path = meme.make_meme(tmp_file, body, author)
    except:
        print('Error creating the meme')

    #remove the temporary image
    try:
        os.remove(tmp_file)
    except:
        print('Error removing temporary image')

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
