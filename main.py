import sys
from stats import word_count, count_characters,sort_dictionary

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    character_count = count_characters(text)
    sorted_dictionary = sort_dictionary(character_count)
    print_report(book_path, num_words, sorted_dictionary)

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def print_report(book_path, num_words, sorted_dictionary):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_dictionary:
        if not item['char'].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


main()
