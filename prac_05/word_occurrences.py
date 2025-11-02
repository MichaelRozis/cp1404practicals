"""
Word Occurrences
Estimate: 25 minutes
Actual:   30 minutes
"""

word_to_count = {}

text = "I really really want to go camping I seriously can not wait to go camping"
words = text.split()
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

max_length = max((len(word) for word in words))
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")