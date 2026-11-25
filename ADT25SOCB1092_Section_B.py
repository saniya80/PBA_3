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

#OUTPUT:
'''Enter a sentence: MIT adt is a well known university, this university has more than 3 branches in pune.
Words that occur more than once:
university: 2
PS C:\Users\n51308\Downloads\PBA_3> & 'C:\Program Files\Python313\python.exe' 'c:/Users/n51308/Downloads/PBA_3/ADT25SOCB1092_Section_B.py'
Enter a sentence: I'm a CSE student
No words occur more than once.
PS C:\Users\n51308\Downloads\PBA_3> '''    