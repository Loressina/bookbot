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