def get_book_text(filepath):
    with open(filepath) as book:
        book_contents = book.read()
        return book_contents

def main(filepath):
    num_words = word_count(filepath)
    num_char = char_count(filepath)
    return num_words, num_char
    #print(book_contents)

def word_count(filepath):
    word_list = get_book_text(filepath)
    num_words = len(word_list.split())
    return num_words
    #print(f"{num_words} words found in the document")

def char_count(filepath):
    word_list = get_book_text(filepath)
    letter_count = {}
    for i in word_list:
        character = i.lower()
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1
    return letter_count

def report(filepath, word_count, letter_count):
    letter_count = dict(sorted(letter_count.items(),key= lambda item: item[1], reverse=True))
    print("============ BOOKBOT ============")
    print(f"Analyzing books found at {filepath}")
    print("------------Word Count------------")
    print(f"Found {word_count} total words")
    print("---------Character Count----------")
    for key,value in letter_count.items():
        print(f"{key}: {value}")


"""Count Characters

Ah, the meat of bookbot: counting characters!
Assignment

    Add a new function to your stats.py file that takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
        Convert any character to lowercase using the .lower() method, we don't want duplicates.
        Use a dictionary of String -> Integer. The returned dictionary should look something like this:

{'p': 6121, 'r': 20818, 'o': 25225, ...

    Import and call the function in main.py, and capture the result in a new variable.
    After printing the word count, print the dictionary of characters and their counts.

Run and submit the CLI tests.
"""
