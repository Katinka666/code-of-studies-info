# imports
from docx import Document
from helper import write_text_units
import logging
import nltk

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

document = Document('./data/code_of_studies.docx')

# slices the document into sentences
def slice_document():
    paragraphs = []
    for para in document.paragraphs:
        paragraphs.append(para.text)
    text = ' '.join(paragraphs)
    sentences = nltk.sent_tokenize(text)
    return sentences

# creates the sentences and writes them to file
def create_sens():
    logging.info("Creating the sentences started...")
    sentences = slice_document()
    write_text_units("sens", sentences)