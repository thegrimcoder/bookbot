from stats import get_num_words, get_num_characters, sort_dictionary
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
            
    return file_contents

def main():
    argv_length = len(sys.argv)
    #print(argv_length)

    if argv_length != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    total_words = get_num_words(get_book_text(sys.argv[1]))
    character_dictionary = get_num_characters(get_book_text(sys.argv[1]))
    sorted_list = sort_dictionary(character_dictionary)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
    
main()                
