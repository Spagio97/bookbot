def get_num_words(book_text):
    words_list = book_text.split()
    return len(words_list)

def get_char_appearances(book_text):
    char_dict = {}
    lower_book_text = book_text.lower()
    char_set = set(lower_book_text)
    for char in char_set:
        char_dict[char] = lower_book_text.count(char)
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_dicts(dict):
    dict_list = []
    for char in dict: 
        dict_list.append({
            "char": char,
            "num": dict[char]
        })
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list
