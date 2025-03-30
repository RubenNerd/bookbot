import sys
from stats import count, count_letters, sort_char_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

    path = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        book_text = f.read()
    return book_text

def main():
    path = sys.argv[1]
    book_text = get_book_text(path)
    word_count = count(book_text)
    character_count = count_letters(book_text)
    sorted_characters = sort_char_count(character_count)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_characters:
        char = char_dict["char"]
        if char.isalpha():
            print(f"{char}: {char_dict['count']}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()


