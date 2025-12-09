import sys
from stats import count_words
from stats import count_symbols
from stats import raport


def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents
    
    
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    counter = count_words(text)
    #print(f'Found {counter} total words')
    all_characters_count = count_symbols(text)
    end_raport = raport(all_characters_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {counter} total words")
    print("--------- Character Count -------")

    for item in end_raport:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f'{char}: {num}')

    print("============= END ===============")



main()