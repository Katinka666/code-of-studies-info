# imports
from transformers import AutoModel
from helper import read_text_units, write_embeddings
import logging

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# calculate the embedding,
# text_units: the list of the document slices (chunks, sentences...)
def calculate_embeddings(text_units):
    logging.info("Calculate embeddings started...")

    # initializing the  model
    logging.info("Initializing the embedding model... this might take some time.")
    embedding_model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-en', trust_remote_code=True) # trust_remote_code is needed to use the encode method
    
    logging.info("Encoding...")
    embeddings = [] # the vector values of each slice
    for text_unit in text_units:
        embedding = embedding_model.encode(text_unit)
        embeddings.append(embedding)
    return embeddings

def embed_text_units(text_unit):
    logging.info(f"Embedding the {text_unit} started...")
    text_units = read_text_units(text_unit)
    embeddings = calculate_embeddings(text_units)
    write_embeddings(text_unit, embeddings)