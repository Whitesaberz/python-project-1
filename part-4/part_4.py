### Step 1 - Input function

## Create five input statements to gather user's book they want to input to the system. After that be sure to turn it into a function.

# Code here

# def create_new_book():
#     title = input("What is the book called? ")
#     author = input("Who wrote the book? ")
#     year = input("What year was the book published? "))
#     rating = input("Out of 5, how would you rate this book? "))
#     pages = input("How many pages does the book have? "))

#     book_info = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_info

# print(create_new_book())

### Step 2 - Type conversion

## Now convert the proper data-types front strings to either floats or ints depending on what it is. Feel free to comment out your old function so you don't get an error, or copy/paste and give it a new name.

# Code here

# def create_new_book():
#     title = input("What is the book called? ")
#     author = input("Who wrote the book? ")
#     year = int(input("What year was the book published? "))
#     rating = float(input("Out of 5, how would you rate this book? "))
#     pages = int(input("How many pages does the book have? "))

#     book_info = {
#         "title": title,
#         "author": author,
#         "year": year,
#         "rating": rating,
#         "pages": pages
#     }

#     return book_info

# print(create_new_book())


### Step 3 - Error handling

## Now take your previous function, and handle potential errors should the user type an answer that doesn't convert data-type properly.

# Code here

def create_new_book():
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
    
    book_info = {
        "title": title,
        "author": author,
        "year": year,
        "rating": rating,
        "pages": pages
    }

    return book_info

# print(create_new_book())

### Step 4 - if/elif/else

## Now create a main menu function that gives the user options. Handle their choices with if/elif/else statements.

# Code here

the_book_list = [{
    "title": "The Fellowship of the Ring",
    "author": "J.R.R. Tolkein",
    "year": 1954,
    "rating": 4.98,
    "pages": 423
},
{
    "title": "The Two Towers",
    "author": "J.R.R. Tolkein",
    "year": 1954,
    "rating": 4.97,
    "pages": 352
},
{
    "title": "The Return of the King",
    "author": "J.R.R. Tolkein",
    "year": 1955,
    "rating": 4.99,
    "pages": 416
},
{
    "title": "The Five People You Meet in Heaven",
    "author": "Mitch Albom",
    "year": 2003,
    "rating": 4.32,
    "pages": 266
},
{
    "title": "Watchmen",
    "author": "Alan Moore",
    "year": 1995,
    "rating": 5,
    "pages": 416
}]

def print_all_books(list_of_books):

    print("\nHere are all your books...\n")

    for book in list_of_books:
        title = book["title"]
        author = book["author"]
        year = book["year"]
        rating = book["rating"]
        pages = book["pages"]

        print(f"Title: {title}, Author: {author}, Year: {year}, Rating: {rating}, Pages: {pages}")

# def main_menu():

#     select = input('Please choose an option: \n"Add" to add a book, \n"Get All" to see all books \n"Done" to close. \nType Here: ').lower()
#     if select == "add":
#         the_book_list.append(create_new_book())
#     elif select == "get all":
#         print(the_book_list)
#     elif select == "done":
#         print("Thank you!")
#     else:
#         print('Please select "add", "get all" or "done". Type Here: ')
# main_menu()


### Step 5 - while loops

## Now add a while loop to your main menu to keep it alive, and continually asking for input until the user chooses to exit the program. Call the main menu to ensure it functions properly.

# Code here

def main_menu():

    in_use = True
    while in_use:
        select = input('Please choose an option: \n"Add" to add a book, \n"Get All" to see all books \n"Done" to close. \nType Here: ').lower()
        if select == "add":
            the_book_list.append(create_new_book())
        elif select == "get all":
            print_all_books(the_book_list)
        elif select == "done":
            print("\nThank you!")
            in_use = False
        else:
            print('Please select "add", "get all" or "done". Type Here: ')

main_menu()