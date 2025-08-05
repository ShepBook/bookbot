import sys
from stats import get_num_words, count_chars, sorted_dicts_from_dict

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def print_report(filepath):
    book_string = get_book_text(filepath)
    word_count = get_num_words(book_string)
    counted_chars = count_chars(book_string)
    sorted_letter_counts = sorted_dicts_from_dict(counted_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for each in sorted_letter_counts:
        print(f"{each['char']}: {each['num']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_report(sys.argv[1])

main()