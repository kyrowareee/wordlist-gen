import string
import random
import os
import sys

def generate_wordlist(min_length, max_length):
    chars = string.ascii_lowercase
    wordlist = []

    for length in range(min_length, max_length + 1):
        for attempt in range(1000):
            word = ''.join(random.choice(chars) for _ in range(length))
            wordlist.append(word)
            print(f"Generated word: {word}, Length: {length}")

    return wordlist

if __name__ == "__main__":
    min_length = int(input("Minimum word length: "))
    max_length = int(input("Maximum word length: "))

    wordlist = generate_wordlist(min_length, max_length)

    output_file = input("Wordlist name: ")
    wordlist_dir = os.path.join(os.path.dirname(__file__), "wordlist")
    os.makedirs(wordlist_dir, exist_ok=True)
    wordlist_path = os.path.join(wordlist_dir, output_file)

    with open(wordlist_path, "w") as wordlist_file:
        for word in wordlist:
            wordlist_file.write(f"{word}\n")

    print(f"Wordlist saved to: {wordlist_path}")
    print(f"Generated {len(wordlist)} words with lengths between {min_length} and {max_length} characters.")

    input("Press Enter to close the script...")
    sys.exit(0)