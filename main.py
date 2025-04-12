from stats import count_words
from stats import count_characters

def get_book_text(filepath):
    with open(filepath) as file:
        return file.read()

def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    char_count = count_characters(book_text)

    print(f"{word_count} words found in the document")
    print(char_count)

main()