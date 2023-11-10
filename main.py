def word_count_of_text(text):
    words = text.split()
    return len(words)


def letter_count_of_text(text):
    letters = {}
    for text_letter in text:
        lower_letter = text_letter.lower()
        text_letter_count = letters.get(lower_letter)
        if text_letter_count is None:
            letters[lower_letter] = 0
        letters[lower_letter] += 1
    return letters


def sort_key(element):
    return element[1]


book_name = "books/frankenstein.txt"
with open(book_name) as f:
    file_contents = f.read()
    word_count = word_count_of_text(file_contents)

    letter_counts = letter_count_of_text(file_contents)
    letter_count_list = []
    for letter in letter_counts:
        letter_count = (letter, letter_counts[letter])
        letter_count_list.append(letter_count)
    letter_count_list.sort(key=sort_key, reverse=True)

    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count} words found in the document")
    print()
    for letter_count in letter_count_list:
        if letter_count[0].isalpha():
            print(f"The '{letter_count[0]}' character was found {letter_count[1]} times")
    print("--- End report ---")
