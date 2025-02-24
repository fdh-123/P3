from transformers import pipeline

# Load the Question-Answering model
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Function to answer questions based on context
def get_answer(question, context):
    result = qa_pipeline(question=question, context=context)
    return result["answer"]

# Example Usage
context = "ChatGPT is an AI model developed by OpenAI, designed for natural language processing tasks."
question = "Who developed ChatGPT?"

print(get_answer(question, context))
