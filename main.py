import sys
from stats import count_words
from stats import count_characters
from stats import sort_char_counts

def get_book_text(filepath):
    try:
        with open(filepath) as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file '{filepath}': {e}")
        sys.exit(1)

def print_report(filepath, word_count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for char_count in char_counts:
        if char_count["char"].isalpha():
            print(f"{char_count["char"]}: {char_count["count"]}")

    print("============= END ===============")

def check_arguments():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def main():
    check_arguments()

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)
    word_count = count_words(book_text)
    char_counts = count_characters(book_text)
    sorted_counts = sort_char_counts(char_counts)

    print_report(filepath, word_count, sorted_counts)

main()