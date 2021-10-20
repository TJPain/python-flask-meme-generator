# Meme Generator
### Udacity Intermediate Python Nanodegree - Large Codebases with Libraries Project

A multimedia command-line and web application to dynamically generate memes, which include an image with an overlaid quote and author name. 

---

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the required environment.

```bash
pip install -r requirements.txt
```

You will also need to install [pdftotext](https://pypi.org/project/pdftotext/)

```bash
pip install pdftotext
```

---

## Running the programme

The programme can be run via the command line or as a web application. 

### Running the programme as a web application

To start the application run app.py on flask:

```bash
python app.py
```

Once running, you can access the application on the following virtual server: http://localhost:5000

### Running the programme using the command line

To run the programme at the command line, invoke `python3 meme.py`. `meme.py`  takes three optional command line arguments:

1. `--path` the path for an image file
2. `--body` the quote body as a string
3. `--author` the author of the quote

The script returns a path to a generated image. If any argument is not defined, a random selection is used.

```bash
$ python3 meme.py

usage: meme.py [-h] [--path PATH] [--body BODY] [--author AUTHOR]
```

---

## Project Components

The project consists of two modules: `QuoteEngine` and `MemeEngine`. 

The `QuoteEngine` module is responsible for ingesting many types of files (pdf, txt, csv, and pdf) that contain quotes, consisting of the quote body and an author. The module consists of the `IngestorInterface` abstract base class; ingestor helper classes for each file type; the `Ingestor` class which selects the appropriate ingestor helper based on the file extension; and the `QuoteModel`, which encapsulates the body of the quote and the author. 

The `MemeEngine` module is responsible for creating the memes by manipulating and drawing text onto images.
