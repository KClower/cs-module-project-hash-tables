import random
import re


# Read in all the words in one go
with open('applications/markov/input.txt') as f:
    words = f.read().split()

# TODO: analyze which words can follow other words
# Your code here
word_followers = {}

for i in range(len(words) - 1):
    current_word = words[i]
    next_word = words[i + 1]
    if current_word not in word_followers:
        word_followers[current_word] = []
    word_followers[current_word].append(next_word)

def is_start_word(word):
    return re.match(r'^["]?[A-Z]', word) is not None

def is_stop_word(word):
    return re.search(r'[.!?]["]?$', word) is not None

# TODO: construct 5 random sentences
# Your code here

for i in range(5):
    start_word = random.choice([word for word in words if is_start_word(word)])
    sentence = [start_word]
    current_word = start_word

while current_word in word_followers and not is_stop_word(current_word):
    next_word = random.choice(word_followers[current_word])
    sentence.append(next_word)
    current_word = next_word

print(" ".join(sentence) + "\n")




