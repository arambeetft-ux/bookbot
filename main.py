def get_book_text(filepath):
    with open(filepath) as  f:
        text = f.read()
    return text

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)  # Print the first 1000 characters of the book

# python
if __name__ == "__main__":
    main()
    