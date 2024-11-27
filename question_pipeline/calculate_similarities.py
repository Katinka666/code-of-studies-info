# imports
import numpy
from numpy.linalg import norm
from helper import read_text_units_embedded, read_questions_embedded
import logging
from pathlib import Path

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# similarity function
cos_sim = lambda a,b: (a @ b.T) / (norm(a)*norm(b))

# calculate similarities
def calculate_similarity_scores(vectors, q_vector):
    logging.info("Calculate similarity scores started...")
    similarities = []
    for vector in vectors:
        similarities.append(cos_sim(numpy.fromstring(q_vector, sep=' '), numpy.fromstring(vector, sep=' ')))
    return similarities

# write similarites to a file
def write_similarities(similarities, q_idx, text_unit):
    logging.info(f"Writing the similarity scores for question {q_idx} started...")

    try:
        with open(f"data/{text_unit}/similarities/q{q_idx}.txt", "w") as file:
            for idx, similarity in enumerate(similarities):
                file.write(str(similarity))
                # unless it was the last score, we need a line break
                if (idx != len(similarities) - 1):
                    file.write("\n")
        logging.info("Successfully wrote the similarity scores to file.")
    except Exception as ex:
        logging.error(f"Writing the similarity scores for question {q_idx} to file was unsuccessful: {ex}")   
        raise

def calculate_and_write_all_similarities(question_vectors, vectors, text_unit):
    logging.info("Calculating and writing all similarity scores to file...")

    # creating the directory if it doesn't exist
    path = Path(f"data/{text_unit}/similarities")
    path.mkdir(exist_ok=True)

    for idx, q_vector in enumerate(question_vectors):
        similarities = calculate_similarity_scores(vectors, q_vector)
        write_similarities(similarities, idx, text_unit)

# text_unit: String that defines the name of the slice of data that we are working with in the pipeline
def calculate_similarities(text_unit):
    logging.info("Calculate similarities started...")
    vectors = read_text_units_embedded(text_unit)
    question_vectors = read_questions_embedded()
    calculate_and_write_all_similarities(question_vectors, vectors, text_unit)