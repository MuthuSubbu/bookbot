from stats import (
    get_num_words, 
    get_characters, 
    report
)
import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    # Sample arguments to pass - python3 main.py /Users/Muthu/learning/python/bookbot/books/frankenstein.txt
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    num_of_words = get_num_words(file_contents)
    #print(f"{r} words found in the document")
    char_count = get_characters(file_contents)
    #print(char_count)
    chars_sorted_list = report(char_count)
    print_report(num_of_words, chars_sorted_list)

def print_report(num_of_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()