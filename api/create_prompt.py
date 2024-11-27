# imports
from helper import read_top_text_units, read_questions, write_prompt
import logging

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# You can work with multiple text units,
# the funtion will collect the relevant ones for the question with the given index
def collect_text_units(text_units_list, q_idx):
    logging.info(f"Collecting text units for question {q_idx}...")
    collected_text_units = []
    for text_unit in text_units_list:
        collected_text_units += read_top_text_units(q_idx, text_unit)
    return collected_text_units

# creates contents prompt messages,
# returns a list with two elements
def create_prompt_for_question(relevant_text_unit_list, question):
    logging.info(f"Creating prompt...")
    system_content = f"You will be given some extract from the university's code of studies, and your task is to answer a student's question based on it. The question: {question}".replace("\n", "").replace("\r", "")
    user_content = " ".join(relevant_text_unit_list).replace("\n", "").replace("\r", "")
    return [system_content, user_content]

# write prompts
def write_prompts(content_list_list):
    logging.info("Writing prompts...")
    for idx, content_list in enumerate(content_list_list):
        write_prompt(idx, content_list)

# text_unit_list: the name of the text units we will work with (chunks, sentences,...)
def create_prompt(text_unit_list):
    logging.info("Create pompt started...")
    questions = read_questions()
    prompts = []
    for idx, question in enumerate(questions):
        relevant_text_unit_list = collect_text_units(text_unit_list, idx)
        prompt = create_prompt_for_question(relevant_text_unit_list, question)
        prompts.append(prompt)
    write_prompts(prompts)