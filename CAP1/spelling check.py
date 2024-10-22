# Function to find incorrect words in a Dzongkha letter
def find_incorrect_words(letter_file, dictionary_file):
    # Read the dictionary into a set for fast lookup
    with open(dictionary_file, 'r', encoding='utf-8') as dict_file:
        dictionary = set(word.strip() for word in dict_file.readlines())

    # Initialize a list to store errors
    errors = []

    # Read the letter file line by line
    with open(letter_file, 'r', encoding='utf-8') as letter:
        for line_number, line in enumerate(letter, start=1):
            words = line.split()
            for word_position, word in enumerate(words, start=1):
                # Check if the word is in the dictionary
                if word not in dictionary:
                    # Record the error (line number, word position, and the word)
                    errors.append((line_number, word_position, word))

    return errors


# Example usage
letter_file = '347.txt'
dictionary_file = 'dictionary.txt'
incorrect_words = find_incorrect_words(letter_file, dictionary_file)

# Print the results
for line, position, word in incorrect_words:
    print(f"Line {line}, Word Position {position}: '{word}' is incorrect.")