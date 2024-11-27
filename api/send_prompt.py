# imports
import os
from dotenv import load_dotenv
import logging
from helper import read_prompt, write_response
from openai import OpenAI

# logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# loading environmental variables to access api key
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    logging.error("No API key found!")
    raise ValueError("No API key found!")

# initializing the client
client = OpenAI()

def get_response(prompt):
    logging.info("Get response started...")
    if len(prompt) != 2:
        logging.error(f"The prompt must contain exactly 2 elements, but it was {len(prompt)}")
        raise ValueError(f"The prompt must contain exactly 2 elements!")
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
            "role": "system",
            "content": prompt[0]
            },
            {
            "role": "user",
            "content": prompt[1]
            }
        ],
        temperature=0.7,
        max_tokens=200,
        top_p=1
    )
    return response.choices[0].message.content

def send_prompt(q_idx):
    logging.info(f"Sending prompt for question with idx {q_idx}")
    prompt = read_prompt(q_idx)
    response = get_response(prompt)
    write_response(q_idx, response)
