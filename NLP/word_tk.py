# import nltk
# from nltk.tokenize import word_tokenize

# # Download resources (first time only)
# nltk.download('punkt')
# nltk.download('punkt_tab')

# text = "i am a gayathri :"

# words = word_tokenize(text)

# print("Original Text:", text)
# print("Word Tokens:", words)






# # character tokenization 

# text = "Natural Language Processing"

# # Character Tokenization
# characters = list(text)

# print("Original Text:")
# print(text)

# print("\nCharacter Tokens:")
# print(characters)






import nltk
from nltk.tokenize import word_tokenize

# Download tokenizer data (run only once)
nltk.download('punkt')

text = "Hello! My name is Gayathri. I am learning NLP."

tokens = word_tokenize(text)

print("Original Text:")
print(text)

print("\nWord Tokens:")
print(tokens)