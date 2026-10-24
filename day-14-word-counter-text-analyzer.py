
import string

text = input("Enter a paragraph: ")

# Count words and characters
words = text.split()
total_words = len(words)
total_characters = len(text)
characters_without_spaces = len(text.replace(" ", ""))

# Count sentences
sentences = 0

for character in text:
    if character in ".!?":
        sentences += 1

# Clean the text for word frequency
clean_text = text.lower()
clean_text = clean_text.translate(
    str.maketrans("", "", string.punctuation)
)

clean_words = clean_text.split()

# Count each word
word_counts = {}

for word in clean_words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# Find the most frequent word
if word_counts:
    most_common_word = max(
        word_counts, key=word_counts.get
    )
else:
    most_common_word = "None"

# Display results
print("\n--- TEXT ANALYSIS ---")
print("Total words:", total_words)
print("Total characters:", total_characters)
print("Characters without spaces:", characters_without_spaces)
print("Estimated sentences:", sentences)
print("Word frequencies:", word_counts)
print("Most frequent word:", most_common_word)
