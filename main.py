def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print("Found " + str(num_words(book_text)) + " total words")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def num_words(book_text):
    words_list = book_text.split()
    return len(words_list)

main()