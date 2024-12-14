# *******
# IMPORTS
# *******

# from preprocess_document.embed_text_units import embed_text_units
# from preprocess_document.chunks.create_chunks import create_chunks
# from preprocess_document.sentences.create_sens import create_sens
# IMPORT CUSTOM SLICER
# from preprocess_questions.embed_questions import embed_questions
# from question_pipeline.pipeline_script import pipeline
# from api.create_prompt import create_prompt
from api.send_prompt import send_prompt

# *******************
# PREPROCESS DOCUMENT
# *******************

# create_chunks()
# embed_text_units("chunks")

# create_sens()
# embed_text_units("sens")

# create_slices() # replace the method with your own implementation 
# embed_text_units("slices") # replace "slices" with the your custom text unit name

# ********************
# PREPROCESS QUESTIONS
# ********************

# # Save your questions in data/questions/questions.txt.
# # Each question should be in a separate line.
# embed_questions()

# ********
# PIPELINE
# ********

# (Note: If necessary, pipeline elements can be run separately.)

# pipeline("chunks", 20, 3)
# pipeline("sens", 20, 3)
# pipeline("slices", 20, 3) # replace it with your custom text unit name and parameters

# *************
# CREATE PROMPT
# *************

# create_prompt(["chunks", "sens"])
# # OR you can include your custom text units as well:
# create_prompt(["chunks", "sens", "slices"]) # replace "slices" with your custom text unit name

# As a parameter, enter the index of the question for which you want the answer.
# Question indexes start with zero!
send_prompt(0)