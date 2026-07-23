# # Domain-Specific Stop Word Removal

# text = """
# Machine learning is a branch of artificial intelligence.
# The model is trained on the dataset to improve prediction accuracy.
# """

# # Tokenize the text
# words = text.lower().split()

# # General stop words
# general_stop_words = {
#     "is", "a", "of", "the", "on", "to", "and", "in"
# }

# # Domain-specific stop words (Machine Learning / NLP)
# domain_stop_words = {
#     "machine", "learning", "model", "dataset"
# }

# # Combine both sets
# all_stop_words = general_stop_words.union(domain_stop_words)

# # Remove stop words
# filtered_words = [word for word in words if word not in all_stop_words]

# print("Original Words:")
# print(words)

# print("\nFiltered Words:")
# print(filtered_words)