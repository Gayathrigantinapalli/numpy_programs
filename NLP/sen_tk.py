import nltk
from nltk.tokenize import sent_tokenize

# Download the required resource (only first time)
# nltk.download("punkt")
# nltk.download("punkt_tab")

# text = """
# Hello everyone. Welcome to NLP.
# Python is easy to learn!
# Let's study sentence tokenization.
# """

# # Sentence Tokenization
# sentences = sent_tokenize(text)

# print("Original Text:")
# print(text)

# print("\nSentence Tokens:")
# for i, sentence in enumerate(sentences, start=1):
#     print(f"{i}. {sentence}")