def count(book_text):
    word_count = 0
    book_text_list = book_text.split()
    for word in book_text_list:
        word_count += 1
    return word_count

def count_letters(book):
    count_letters = {}
    words = book.split()
    
    for letter in words:
        characters = letter.lower()
        for char in characters:
                if char in count_letters:
                    count_letters[char] += 1
                else:
                    count_letters[char] = 1
    return count_letters

def sort_char_count(counts):
    count_list = []
    for char, count in counts.items():
        count_list.append({
            "char": char,
            "count": count
        })
    count_list.sort(reverse=True, key=lambda dict: dict["count"])
    return count_list