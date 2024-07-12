def main():                                                     # main code brackt
    book_path = "books/frankenstein.txt"                        # defines the path to the books
    text = get_book_text(book_path)                             # return the book from the file
    num_words = get_num_words(text)                             # return the number of words in the book
    character_count = get_char_count(text)                      
    print(f"{num_words} words found in the document")           # print our the message

def get_num_words(text):                                        # code for word cound in the book
    words = text.split()                                        # spliting the book in to separate words
    return len(words)                                           # returning word count from the book

def get_book_text(book_path):                                   # code for reading the book
    with open(book_path) as f:                                  # 
        return f.read()                                         #
    
def get_char_count(text):
    lowercase_char = text.lower()
    import collections
    char_count = collections.Counter (lowercase_char)
    sorted_char_count = dict(sorted(char_count.items()))
    print (sorted_char_count)

main()