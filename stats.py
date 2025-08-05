def get_num_words(s):
    list_of_words = s.split()
    word_count = len(list_of_words)
    return word_count

def count_chars(s):
    character_count = {}
    lowercase_string = s.lower()
    for letter in lowercase_string:
        if letter.isalpha():
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1
    return character_count

def sort_on(items):
    return items["num"]

def sorted_dicts_from_dict(dict):
    list_of_dicts = []
    for entry in dict:
        list_of_dicts.append({"char": entry, "num": dict.get(entry)})
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts