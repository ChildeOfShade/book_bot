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

def print_character_counts(c_count):
    sorted_chars = sorted(c_count.items(), key=lambda item: item[1], reverse=True)

    for char, count in sorted_chars:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")