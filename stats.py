def get_num_words(str):
    return len(str.split())

def get_num_characters(str):
    characters = str.lower()

    char_count = {}

    for char in characters:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_Dictionary(dict):
    return 10