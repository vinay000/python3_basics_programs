import re

def tokenize(text): 
    return re.findall(r'\w+', text.lower())

profane_tokens = {"nerfherder"}

sentence = "Why you stuck-up, half-witted, scruffy-looking nerfherder!"

tokens = tokenize(sentence)
print(tokens)

# Rate: number of occurrences normalized by total number
degree_of_profanity = sum(1 for t in tokens if t in profane_tokens) / len(tokens)
print(degree_of_profanity)