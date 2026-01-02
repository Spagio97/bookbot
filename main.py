from stats import get_num_words, get_char_appearances, sorted_dicts

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    char_dict = get_char_appearances(book_text)
    sorted_dict = sorted_dicts(char_dict)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")    
    print("Found " + str(get_num_words(book_text)) + " total words")
    print("--------- Character Count -------")
    for dict in sorted_dict:
        if dict["char"].isalpha() == True:
            print (dict["char"] + ": " + str(dict["num"]))
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()