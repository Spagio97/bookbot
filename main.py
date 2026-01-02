from stats import get_num_words, get_char_appearances

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print("Found " + str(get_num_words(book_text)) + " total words")
    print (get_char_appearances(book_text))

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()