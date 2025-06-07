from stats import count_words, count_characters, print_character_counts
def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

book_path = "books/frankenstein.txt"
    
def main():
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_character_counts(char_count)
    

if __name__ == "__main__":
    main()
