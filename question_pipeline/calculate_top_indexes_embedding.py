# imports
from helper import read_text_unit_similarities, read_questions
import logging
from pathlib import Path

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def write_top_x_embedding(indexes, q_idx, text_unit):
    logging.info(f"Writing the top embedding indexes for question {q_idx}...")

    try:
        with open(f"data/{text_unit}/top_indexes_embedding/q{q_idx}.txt", "w") as file:
            for idx, index in enumerate(indexes):
                file.write(str(index))
                # unless it was the last score, we need a line break
                if (idx != len(indexes) - 1):
                    file.write("\n")
    except Exception as ex:
        logging.error(f"Writing top embedding indexes for question {q_idx} was unsuccessful: {ex}")
        raise

def calculate_top_x_embedding(q_idx, text_unit, top_x):
    logging.info(f"Calculating top {top_x} indexes...")
    similarities = read_text_unit_similarities(q_idx, text_unit)
    indexed_score_list = list(enumerate(similarities)) # creates pairs of (index, value)
    sorted_score_list = sorted(indexed_score_list, key=lambda x: x[1], reverse=True) # sorts the list by descending order
    top_x_idx = [x[0] for x in sorted_score_list[:top_x]]
    return top_x_idx

def calculate_top_indexes_embedding(text_unit, top_x):
    logging.info(f"Calculating top {top_x} indexes for embedded {text_unit}...")
    questions = read_questions()
    
    # creating the directory if it doesn't exist
    path = Path(f"data/{text_unit}/top_indexes_embedding")
    path.mkdir(exist_ok=True)

    for idx, question in enumerate(questions):
        indexes = calculate_top_x_embedding(idx, text_unit, top_x)
        write_top_x_embedding(indexes, idx, text_unit)