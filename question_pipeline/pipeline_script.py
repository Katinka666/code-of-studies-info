# 1. calculate similarities
# 2. calculate top embeddings (output: chunk indexes)
# 3. calculate top rerankings (output: chunks)

# imports
import question_pipeline.calculate_similarities as similarity
import question_pipeline.calculate_top_indexes_embedding as embedding
import question_pipeline.calculate_top_text_units_reranking as reranking

def pipeline(text_unit, top_x, top_y):
    similarity.calculate_similarities(text_unit)
    embedding.calculate_top_indexes_embedding(text_unit, top_x)
    reranking.calculate_top_text_units_reranking(text_unit, top_y)