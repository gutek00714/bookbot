from stats import count_words
from stats import count_symbols


def get_book_text(file_path):
    with open(file_path, encoding="utf-8") as f:
        file_contents = f.read()
        return file_contents
    
    
def main():
    frankenstein_path = './books/frankenstein.txt'
    text = get_book_text(frankenstein_path)
    counter = count_words(text)
    print(f'Found {counter} total words')
    all_characters_count = count_symbols(text)
    print(all_characters_count)

main()