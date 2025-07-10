from stats import get_num_words, get_num_characters, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
            
    return file_contents

def main():
    total_words = get_num_words(get_book_text("./books/frankenstein.txt"))
    character_dictionary = get_num_characters(get_book_text("./books/frankenstein.txt"))
    sorted_list = sort_dictionary(character_dictionary)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_list:
        if dict['char'].isalpha():
            print(f"{dict['char']}: {dict['num']}")
    print("============= END ===============")
    
main()                
