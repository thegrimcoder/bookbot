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

def sort_dictionary(dict):
    sorted_list = []
    keys = dict.keys()

    for key in keys:
        temp_dict = {}
        temp_dict[char] = key
        temp_dict[num] = dict[key]
        sorted_list.append(temp_dict)

    sorted_list.sort(key="num")
    return sorted_list
