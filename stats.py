def word_count(book_text_string):
    words = book_text_string.split()
    return len(words)

def count_characters(book_text_string):
    characters = list(book_text_string)
    character_dictionary = {}
    for character in characters:
        lower_case_character = character.lower()
        if lower_case_character in character_dictionary:
            character_dictionary[lower_case_character] += 1
        else:
            character_dictionary[lower_case_character] = 1
    return character_dictionary

def sort_on(items):
    return items["num"]

def sort_dictionary(char_dictionary):
    sorting_dictionary = []
    for ch, num in char_dictionary.items():
        sorting_dictionary.append({"char": ch, "num": num})
    sorting_dictionary.sort(reverse=True, key=sort_on)
    #print(sorted_dictionary)
    return sorting_dictionary
