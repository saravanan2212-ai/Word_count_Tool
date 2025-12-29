from collections import Counter
import string

try:
    with open("sample_text.txt", "r") as file:
        text = file.read()
except FileNotFoundError:
    print("File illa da, check pannunga!")
    exit()

# Count lines, words, characters
lines = text.split("\n")
num_lines = len(lines)

words = text.split()
num_words = len(words)

num_chars = len(text)

# Word frequency analysis
clean_text = text.translate(str.maketrans('', '', string.punctuation)).lower()
words_list = clean_text.split()
word_counts = Counter(words_list)

# Display structured results
print("\n--- Word Count Analysis ---")
print(f"Number of lines: {num_lines}")
print(f"Number of words: {num_words}")
print(f"Number of characters: {num_chars}")

print("\nTop 10 Most Common Words:")
for word, count in word_counts.most_common(10):
    print(f"{word}: {count}")
