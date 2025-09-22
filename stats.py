def get_book_text(book):
    relative_file = './books/' + book
    with open(relative_file) as b:
        return b.read()

def get_split_words(book):
    review_book = get_book_text(book).replace('\n', ' ')
    split_list = review_book.split(' ')
    reduced_list = []
    for w in split_list:
        if w.strip():
            reduced_list.append(w)
    return reduced_list

def get_num_words(book):
    clean_book = get_split_words(book)     
    word_count = len(clean_book)
    return word_count

def get_num_letter(book):
    review_words = get_split_words(book)
    letter_dictionary = {}
    for w in range(0, len(review_words)):
        word_list = []
        word_list = review_words[w]
        for l in range(0, len(word_list)):
            if word_list[l].lower() in letter_dictionary:
                letter_dictionary[word_list[l].lower()] += 1
            else:
                letter_dictionary[word_list[l].lower()] = 0
                letter_dictionary[word_list[l].lower()] += 1
    return letter_dictionary

def sort_on(items):
    sorted_items = dict(sorted(items.items(), key=lambda item: item[1], reverse = True))
    return sorted_items