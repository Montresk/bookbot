import sys
def get_book_text(filepath):
        with open(filepath) as f:
                file_contents=f.read()
                return file_contents
def count_words(book_text):
        split_book=book_text.split()
        word_count=len(split_book)
        print(f"Found {word_count} total words")
def sort_on(items):
	return items["num"]
def count_character(book_text):
	char_dict={}
	char_sort=[]
	key_val_dict={}
	for character in book_text:
		character=character.lower()
		if character not in char_dict:
			char_dict[character] = 1
		else: char_dict[character] += 1
	for key, value in char_dict.items():
		if key.isalpha():
			current_char={"char": key, "num": value}
			char_sort.append(current_char)
	char_sort.sort(reverse=True, key=sort_on)
	return char_sort
