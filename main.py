from stats import main, report
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]
#filepath = 'books/frankenstein.txt'
word_Count, char_Count = main(filepath)
print(word_Count)
print(char_Count)
report(filepath, word_Count, char_Count)
