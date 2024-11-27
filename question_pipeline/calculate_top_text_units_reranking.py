# imports

from helper import read_top_text_unit_embedding_indexes, read_text_unit_list_by_index_list, read_questions
from sentence_transformers import CrossEncoder # jina reranker
import logging
from pathlib import Path

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_top_y_text_units(question, q_idx, text_unit, top_y, reranking_model):
    logging.info(f"Calculating top {top_y} {text_unit} for question {q_idx}...")
    indexes_embedding = read_top_text_unit_embedding_indexes(q_idx, text_unit)
    top_text_unit_list_embedding = read_text_unit_list_by_index_list(indexes_embedding, text_unit)
    documents_reranking = reranking_model.rank(question, top_text_unit_list_embedding, return_documents=True, top_k = top_y)
    top_text_unit_list_reranking = []
    for document in documents_reranking:
        top_text_unit_list_reranking.append(document['text'])
    return top_text_unit_list_reranking

def write_top_y_text_units(text_unit_list, q_idx, text_unit):
    logging.info(f"Writing top {text_unit} for question {q_idx}...")

    try:
        with open(f"data/{text_unit}/top_{text_unit}_reranking/q{q_idx}.txt", "w") as file:
            for idx, unit in enumerate(text_unit_list):
                file.write(unit.replace("\n", "").replace("\r", "")) #removind the line breaks as well
                # unless it was the last score, we need a line break
                if (idx != len(text_unit_list) - 1):
                    file.write("\n")
    except Exception as ex:
        logging.error(f"Writing the top {text_unit} was unsuccessful: {ex}")
        raise


def calculate_top_text_units_reranking(text_unit, top_y):
    logging.info(f"Calculate to {top_y} {text_unit} with reranking started...")

    # initialize the jina reranker
    logging.info("Initializing the reranker started. This might take some time...")
    reranking_model = CrossEncoder("jinaai/jina-reranker-v1-tiny-en", trust_remote_code=True)

    questions = read_questions()

    # creating the directory if it doesn't exist
    path = Path(f"data/{text_unit}/top_{text_unit}_reranking")
    path.mkdir(exist_ok=True)

    for idx, question in enumerate(questions):
        top_k_text_units = calculate_top_y_text_units(question, idx, text_unit, top_y, reranking_model)
        write_top_y_text_units(top_k_text_units, idx, text_unit)