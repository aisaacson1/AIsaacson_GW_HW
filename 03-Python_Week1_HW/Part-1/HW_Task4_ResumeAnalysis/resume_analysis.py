# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import string
import nltk
nltk.download('stopwords')
nltk.download('punkt')

from nltk.corpus import stopwords

# Counter is used later in the program
from collections import Counter
#from string import punctuation

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

# Paths
resume_path = os.path.join(".", "Resources", 'resume.md')

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r", encoding = 'utf-8') as resume_file_handler:
        return resume_file_handler.read().lower().split()

# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()

# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation
#print(resume)

# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
print("=============")
print(resume & REQUIRED_SKILLS)


# Calculate the Desired Skills Match using Set Intersection
print("\nDESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)

# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
#print(word_count)

# Using collections.Counter
word_counter = Counter(word_list)
#print(word_counter)

# Comparing both word count solutions
#print(word_count == word_counter)

# Top 10 Words
print("\nTop 10 Words")
print("=============")

# Don't worry about the underscore in front of _word_count
# It is just convention for internal use only
# More info here: https://dbader.org/blog/meaning-of-underscores-in-python

# Clean Punctuation

resume_no_punct = strip_punctuation(str(word_list))
#print(resume_no_punct)

_word_count = len(resume_no_punct.split())
#print(_word_count)

# Clean Stop Words
stop_words = stopwords.words('english')
word_tokens = nltk.word_tokenize(str(resume_no_punct))
filtered_resume = [w for w in word_tokens if w not in stop_words]
#print(filtered_resume)


_word_count1 = {}.fromkeys(filtered_resume, 0)
for word in filtered_resume:
    _word_count1[word] += 1
#print(_word_count1)

# Sort words by count and print the top 10
top10 = top.most_common(10)
top = Counter(_word_count1)

#print("\nTop 10 words used in resume:\n")

for i in top10:
    print(i[0],":",i[1],"\n")
