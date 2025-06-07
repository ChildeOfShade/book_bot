def count_words(words):
    num_words = words.split()
    return len(num_words)

def count_characters(text):
    char_count = {}
    for char in text.lower():  # Convert to lowercase
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
