def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def count_words(words):
    num_words = words.split()
    return len(num_words)


def main():
    book_text = get_book_text("books/frankenstein.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in the document!")

if __name__ == "__main__":
    main()
