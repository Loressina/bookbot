def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_counts = {}
    for char in list(text):
        lchar = char.lower()
        if lchar in char_counts:
            char_counts[lchar] += 1
        else:
            char_counts[lchar] = 1

    return char_counts

def sort_char_dict(dict):
    return dict["count"]

def sort_char_counts(char_counts):
    sorted_counts = []
    for char in char_counts:
        sorted_counts.append({"char": char, "count": char_counts[char]})

    sorted_counts.sort(reverse = True, key = sort_char_dict)

    return sorted_counts