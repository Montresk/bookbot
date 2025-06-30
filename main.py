import sys
from stats import get_book_text, count_words, count_character, sort_on
if len(sys.argv) < 2:
	print("Usage: python3 main.py <path_to_book>")
	sys.exit(1)
book_path=sys.argv[1]
book_text=get_book_text(book_path)
print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
count_words(book_text)
print("--------- Character Count -------")
character_counts = count_character(book_text)
for item in character_counts:
    if item["char"].isalpha():
        print(f"{item['char']}: {item['num']}")
print("============= END ===============")
