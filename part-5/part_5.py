### Step 1 - Store data in a .txt

## This step's instructions explains how to use the open() function, to write and read info from a .txt file. Follow the instructions to create and call a function to add a book, based off of the previous dictionaries for our library, to the .txt file properly formatted with commas as separators.

# Code here


### Step 2 - Read data from a .txt

## Now take your previously create function which prints info about all the books in your library, but gets the info from a list, and make it work by reading the information in your home library's .txt document. This will take some new logic, but you can do it.

# Code here


### Step 3 - if __name__ == "__main__":

## Wrap your main menu function call in an "if __name__ == '__main__':" statement to ensure it doesn't accidentally run if this file is imported as a module elsewhere.

# Code this at the bottom of the script


### Step 4 - Expand and refactor

## Now follow the instructions in this final step. Expand your project. Clean up the code. Make your application functional. Great job getting your first Python application finished!

def main_menu(source):

    in_use = True
    while in_use:
        select = input('Please choose an option: \n"Add" to add a book, \n"Get All" to see all books \n"Pages Total" to get entire library page total \n"Order by year" to get books in chronological order \n"Author Search" to find books by author \n"Done" to close. \nType Here: ')
        if select.lower() == "add":
            create_new_book(source)
        elif select.lower() == "get all":
            show_list_of_books(source)
        elif select.lower() == "pages total":
            total_num_of_pages(source)
        elif select.lower() == "order by year":
            show_books_by_published_year(source)
        elif select.lower() == "author search":
            show_books_by_author(source)
        elif select.lower() == "done":
            print("\nThank you!")
            in_use = False
        else:
            print('\nPlease select one of the options listed\n ')

def create_new_book(source):
    title = input("What is the book called? ")
    author = input("Who wrote the book? ")
    try:
        year = int(input("What year was the book published? "))
    except:
        year = int(input("Please enter a number. "))
    try:
        rating = float(input("Out of 5, how would you rate this book? "))
    except:
        rating = float(input("Please enter a number. "))
    try:
        pages = int(input("How many pages does the book have? "))
    except:
        pages = int(input("Please enter a number. "))
    
    with open(source, "a") as file:
       file.write(f"{title}, {author}, {year}, {rating}, {pages}\n")


def book_list_of_dictionaries(source):
    books_list = []
    with open(source, "r") as f:
        file = f.readlines()
        for line in file:
            title, author, year, rating, pages = line.split(", ")
            books_list.append({
                "title": title,
                "author": author,
                "year": int(year),
                "rating": float(rating),
                "pages": int(pages)
            })
    return books_list

def print_book(book):
    print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Rating: {book['rating']}, Pages: {book['pages']}\n")

def show_list_of_books(source):
    print("\nYour list of books:\n")
    for book in book_list_of_dictionaries(source):
        print_book(book)

def total_num_of_pages(source):
    print(f"\nYour total number of pages in this library is {sum([x['pages'] for x in book_list_of_dictionaries(source)])}\n")

def show_books_by_published_year(source):
    print(f"\nShowing books in chronological order:\n")
    list = book_list_of_dictionaries(source)
    list =  sorted(list, key=lambda x: int(x["year"]))
    for book in list:
        print_book(book)

# The author search feature is something I just wanted to try, if you type the author exactly then it works correctly, I'm unsure how to implement a catch all for this type of feature.

def show_books_by_author(source):
    author_search = input("Which author?")
    print(f"\nBooks by {author_search}:\n")
    list = book_list_of_dictionaries(source)
    list =  sorted(list, key=lambda x: (x["author"]))
    for book in list:
        if book["author"] == author_search:
            print_book(book)
        elif book["author"] != author_search:
            pass
        

if __name__ == "__main__":
    main_menu("library.txt")