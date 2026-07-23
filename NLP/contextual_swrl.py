# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize

# # Run these only once
# nltk.download('punkt')
# nltk.download('stopwords')

# text = "The movie is not good but it is very interesting."

# # Tokenize the sentence
# words = word_tokenize(text)

# # Load stop words
# stop_words = set(stopwords.words('english'))

# # Keep important contextual words
# important_words = {"not", "no", "never"}

# # Remove stop words except important contextual words
# filtered_words = [
#     word for word in words
#     if word.lower() not in stop_words or word.lower() in important_words
# ]

# print("Original Words:")
# print(words)

# print("\nAfter Contextual Stop Word Removal:")
# print(filtered_words)