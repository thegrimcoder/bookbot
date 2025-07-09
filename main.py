from stats import get_num_words

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
            
    return file_contents

def main():
    total_words = get_num_words(get_book_text("./books/frankenstein.txt"))
    print(f"{total_words} words found in the document")
    
main()                