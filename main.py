from stats import get_num_words, get_num_characters, sort_dictionary

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
            
    return file_contents

def main():
    total_words = get_num_words(get_book_text("./books/frankenstein.txt"))
    character_dictionary = get_num_characters(get_book_text("./books/frankenstein.txt"))
    sorted_list = sort_dictionary(character_dictionary)
    print(f"{total_words} words found in the document")
    print(sorted_list)
    
main()                
