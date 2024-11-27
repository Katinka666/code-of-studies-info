from pathlib import Path
import logging

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# name of the directory where the data is stored
data_dir = "data" 

# writes the text units to file (text_unit is the name )
def write_text_units(text_unit_name, text_unit_list):
    logging.info(f"Writing {text_unit_name}...")
    path = Path(f"{data_dir}/{text_unit_name}")
    path.mkdir(exist_ok=True)
    try:
        with open(f"{data_dir}/{text_unit_name}/{text_unit_name}.txt", "w") as file:
            for piece in text_unit_list:
                file.write(piece)
                # unless it was the last piece, we need a line break
                if (text_unit_list.index(piece) != len(text_unit_list) - 1):
                    file.write("\n")
        logging.info(f"Successfully wrote {text_unit_name} to file.")
    except Exception as ex:
        logging.error(f"Writing {text_unit_name} to file was unsuccessful: {ex}")
        raise

# reads the text units from file (like chunks, sentences, ...)
# returns a list of strings
def read_text_units(text_unit_name):
    logging.debug(f"Reading {text_unit_name}...")
    try:
        with open(f"{data_dir}/{text_unit_name}/{text_unit_name}.txt", "r") as file:
            lines = file.readlines()
            return lines
    except Exception as ex:
        logging.error(f"Reading {text_unit_name} from file was unsuccessful: {ex}")
        raise

# reads the questions from file
def read_questions():
    logging.debug("Reading the questions...")
    try:
        with open(f"{data_dir}/questions/questions.txt", "r") as file:
            lines = file.readlines()
            return lines
    except Exception as ex:
        logging.error(f"Reading questions from file was unsuccessful: {ex}")
        raise

# reads the embedded units of text from file
def read_text_units_embedded(text_unit):
    logging.debug(f"Reading embedded {text_unit}...")
    try:
        with open(f"{data_dir}/{text_unit}/{text_unit}_embedded.txt", "r") as file:
            lines = file.readlines()
            return lines
    except Exception as ex:
        logging.error(f"Reading the embeddeded {text_unit} from file was unsuccessful: {ex}")
        raise

# reads the embedded questions from file
def read_questions_embedded():
    logging.debug("Reading embedded questions...")
    vectors = []
    try: 
        with open(f"{data_dir}/questions/questions_embedded.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                vectors.append(line)
            file.close()
            return vectors
    except Exception as ex:
        logging.error(f"Reading the embeddeded questions from file was unsuccessful: {ex}") 
        raise

# reads the similarity scores for a given text unit
def read_text_unit_similarities(q_idx, text_unit):
    logging.debug(f"Reading the {text_unit} similarity scores for question {q_idx}...")
    try:
        with open(f"{data_dir}/{text_unit}/similarities/q{q_idx}.txt", "r") as file:
            lines = file.readlines()
            file.close()
            return lines
    except Exception as ex:
        logging.error(f"Reading the {text_unit} similarity scores for question {q_idx} was unsuccessful: {ex}")
        raise

# read the top embedding indexes of units of text from file
def read_top_text_unit_embedding_indexes(q_idx, text_unit):
    logging.debug(f"Reading the top {text_unit} indexes for question {q_idx}...")
    try: 
        with open(f"{data_dir}/{text_unit}/top_indexes_embedding/q{q_idx}.txt", "r") as file:
            lines = file.readlines()
            file.close()
            return lines
    except Exception as ex:
        logging.error(f"Reading the {text_unit} top indexes for question {q_idx} was unsuccessful: {ex}")
        raise

# read the units of text according to the indexes
def read_text_unit_list_by_index_list(idx_list, text_unit):
    logging.debug(f"Converting index list to {text_unit} list...")
    text_units = []
    try: 
        with open(f"{data_dir}/{text_unit}/{text_unit}.txt", "r") as file:
            lines = file.readlines()
            file.close()
            for idx in idx_list:
                text_units.append(lines[int(idx)])
            return text_units
    except Exception as ex:
        logging.error(f"Reading the element of {text_unit} for index was unsuccessful: {ex}")
        raise 

# read the top text units for a question index
# (this can be used in the prompt!)
def read_top_text_units(q_idx, text_unit):
    logging.debug(f"Reading the top {text_unit} for question {q_idx}...")
    try: 
        with open(f"{data_dir}/{text_unit}/top_{text_unit}_reranking/q{q_idx}.txt", "r") as file:
            lines = file.readlines()
            file.close()
            return lines
    except Exception as ex:
        logging.error(f"Reading the top {text_unit} for question {q_idx} was unsuccessful: {ex}")
        raise

# writes the prompt to file,
# content_list must contain two strings!
def write_prompt(q_idx, content_list):
    logging.info(f"Writing prompt for question {q_idx}...")
    if len(content_list) != 2:
        raise ValueError(f"Content_list must contain exactly 2 strings, but found {len(content_list)}")
    path = Path(f"{data_dir}/prompts")
    path.mkdir(exist_ok=True)
    try:
        with open(f"{data_dir}/prompts/q{q_idx}.txt", "w") as file:
            file.write(f"{content_list[0]}\n{content_list[1]}")
        logging.info(f"Successfully wrote prompt for question {q_idx} to file.")
    except Exception as ex:
        logging.error(f"Writing prompt for question {q_idx} to file was unsuccessful: {ex}")
        raise

# read prompt for the question with the given index
def read_prompt(q_idx):
    logging.debug(f"Reading prompt for question {q_idx}...")
    try: 
        with open(f"{data_dir}/prompts/q{q_idx}.txt", "r") as file:
            lines = file.readlines()
            return lines
    except Exception as ex:
        logging.error(f"Reading the prompt for question {q_idx} was unsuccessful: {ex}")
        raise 

# write response for question with the given index
def write_response(q_idx, response):
    logging.info(f"Writing response for question {q_idx}...")
    path = Path(f"{data_dir}/responses")
    path.mkdir(exist_ok=True)
    try:
        with open(f"{data_dir}/responses/q{q_idx}.txt", "w") as file:
            file.write(response)
        logging.info(f"Successfully wrote response for question {q_idx} to file.")
    except Exception as ex:
        logging.error(f"Writing response for question {q_idx} to file was unsuccessful: {ex}")
        raise

# write the embeddings to file,
# text_unit: the name of the text unit we are working with
def write_embeddings(text_unit, embeddings):
    logging.info("Writing the embeddings to file started...")

    try:
        with open(f"{data_dir}/{text_unit}/{text_unit}_embedded.txt", "w") as file:
            for idx, embedding in enumerate(embeddings):
                for num in embedding:
                    file.write(str(num))
                    file.write(" ")
                # unless it was the last vector, we need a line break
                if (idx != len(embeddings) - 1):
                    file.write("\n")
    except Exception as ex:
        logging.error(f"Writing the embeddings to file was unsuccessful: {ex}")
        raise