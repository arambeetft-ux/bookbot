import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(f):
    file_content = f.read()
    return file_content

from stats import get_num_words, char_num, sort_dict

def main():
    with open(sys.argv[1]) as f:
        text = get_book_text(f)
        num_words = get_num_words(text)
        Char_Dict = char_num(text)
        CharCount = sort_dict(Char_Dict)
    print ("============ BOOKBOT ============")
    print (f"Analyzing book found at {sys.argv[1]}...")
    print ("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print ("------- Character Count --------")
    for char in CharCount:
        if char["char"].isalpha():
            print(f"{char['char']}: {char['num']}")
    print ("============= END ===============")
    






main()

    