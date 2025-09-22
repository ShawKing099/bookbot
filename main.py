import stats as s
import sys

def main():
    if len(sys.argv) == 1:
        print(f'Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    for b in range(1, len(sys.argv)):
        directory = sys.argv[b][0:5]
        read_book = sys.argv[b][6:]
        letter_list = s.get_num_letter(read_book)
        sorted_letters = s.sort_on(letter_list)
        word_count = s.get_num_words(read_book)
        key_list = list(sorted_letters.keys())
        print(f'============ BOOKBOT ============')
        print(f'Analyzing book found at {directory}{read_book}...')
        print(f'----------- Word Count ----------')
        print(f'Found {word_count} total words')
        print(f'--------- Character Count -------')
        for k in range(0, len(sorted_letters)):
            if key_list[k].isalpha():
                key = key_list[k]
                value = sorted_letters[key_list[k]]
                print(f'{key}: {value}')
        print(f'============= END ===============')    

main()
