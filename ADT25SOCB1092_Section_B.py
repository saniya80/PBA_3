import re
from collections import Counter

sentence = input("Enter a sentence: ")
words = re.findall(r"\b\w+\b", sentence.lower())
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

duplicates = {}
for word, count in word_counts.items():
    if count > 1:
        duplicates[word] = count

if duplicates:
    print("Words that occur more than once:")
    for word, count in duplicates.items():
        print(f"{word}: {count}")
else:
    print("No words occur more than once.")