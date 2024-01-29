import itertools

def get_book_text(stellage_number, book_number):
    # We get the symbols that make up the book
    characters = get_characters(stellage_number, book_number)
    
    # Converting characters to text
    text = ''.join(characters)
    
    return text

def get_characters(stellage_number, book_number):
    # We get all possible symbols for this rack
    all_characters = get_all_characters(stellage_number)
    
    # We get the symbols that make up the book
    book_characters = get_book_characters(all_characters, book_number)
    
    return book_characters

def get_all_characters(stellage_number):
    # We get all possible symbols for this rack
    # For example, for rack number 1, it will be all the letters of the alphabet, punctuation marks and dots
    # You need to determine which symbols to include in each rack
    # and implement the appropriate logic here

    # We will return all possible characters consisting of as many letters as are equal to the number of the rack
    return list(itertools.product('abcdefghijklmnopqrstuvwxyz., ', repeat=stellage_number))

def get_book_characters(all_characters, book_number):
    # We get the characters that make up the book
    # For example, if there are 100 characters in the shelf and the book number is 1,
    # then the first book will consist of the first character in the all_characters list

    # Check that the book number does not exceed the number of characters in the rack
    if book_number > len(all_characters):
        raise ValueError('Invalid book number')
    
    # We get the characters that make up the book
    book_characters = list(all_characters[book_number - 1])
    
    return book_characters

# Example of usage
stellage_number = int(input("Enter the rack number: "))
book_number = int(input("Enter the book number: "))
book_text = get_book_text(stellage_number, book_number)
print("Book: ",book_text,sep="\n")
