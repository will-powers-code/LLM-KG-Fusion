# from transformers import AutoTokenizer
# import transformers
# import torch
# from transformers import AutoModelForQuestionAnswering
# from transformers import pipeline


# model_checkpoint = "huggingface-course/bert-finetuned-squad"

# question_answerer = pipeline("question-answering", model=model_checkpoint)

# print(question_answerer(question="Who is John Voight?"))

from transformers import pipeline

question_answerer = pipeline(task="text-generation")
preds = question_answerer("John Voight's mother is?")
print(preds)