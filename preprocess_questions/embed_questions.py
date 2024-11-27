# imports
from transformers import AutoModel
from helper import read_questions
import logging

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# calculate the embedding 
def calculate_embeddings(questions):
    logging.info("Calculate the question embeddings started...")

    # initializing the embedding model
    logging.info("Initializing the embedding model... this might take some time.")
    embedding_model = AutoModel.from_pretrained('jinaai/jina-embeddings-v2-base-en', trust_remote_code=True) # trust_remote_code is needed to use the encode method

    logging.info("Encoding the questions...")
    embeddings = [] # the vector values of each question
    for question in questions:
        embedding = embedding_model.encode(question)
        embeddings.append(embedding)
    return embeddings

# write the embeddings to file
def write_embeddings(embeddings):
    logging.info("Writing the embedded questions to file started...")
    try:
        with open("data/questions/questions_embedded.txt", "w") as file:
            for idx, embedding in enumerate(embeddings):
                for num in embedding:
                    file.write(str(num))
                    file.write(" ")
                # unless it was the last vector, we need a line break
                if (idx != len(embeddings) - 1):
                    file.write("\n")
    except Exception as ex:
        logging.error(f"Writing the question embeddings to file was unsuccessful: {ex}")
        raise

# embed questions
def embed_questions(): 
    questions = read_questions()
    write_embeddings(calculate_embeddings(questions))