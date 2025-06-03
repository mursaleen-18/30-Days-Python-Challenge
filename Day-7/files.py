from collections import Counter
import string

def count_word_frequencies(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()

    # Remove punctuation and convert to lowercase
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator).lower()

    words = cleaned_text.split()

    # Count word frequencies
    word_counts = Counter(words)

    # Print results
    for word, count in word_counts.items():
        print(f"{word}: {count}")

# Example usage
count_word_frequencies('new.txt')
