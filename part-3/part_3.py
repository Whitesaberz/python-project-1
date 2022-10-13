my_book = {
    "title": "The Hunger Games",
    "author": "Suzanne Collins",
    "year": 2008,
    "rating": 4.32,
    "pages": 374
}
the_book_list = {
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
}


# Follow the instructions in this part of the project. Define and flesh out your function below, which should accept a dictionary as an argument when called, and return a string of the info in that book-dictionary in a user-friendly readable format.

# Code below

def sort_book_info(book_info):
    book_string = f"{book_info['title']} was written by {book_info['author']}, published in {book_info['year']}, received a rating of {book_info['rating']}. It is {book_info['pages']} pages long."
    return(book_string)

print(sort_book_info(my_book))


# Once you are finished with that function, create several more functions which return individual pieces of information from the book.

# Code below

def show_book_title(book_info):
    book_title = book_info['title']
    print(book_title)
    return book_title

show_book_title(my_book)

def show_book_author(book_info):
    book_author = book_info['author']
    print(book_author)
    return book_author

show_book_author(my_book)

def show_book_year(book_info):
    book_year = book_info['year']
    print(book_year)
    return book_year

show_book_year(my_book)

def show_book_rating(book_info):
    book_rating = book_info['rating']
    print(book_rating)
    return book_rating

show_book_rating(my_book)

def show_book_pages(book_info):
    book_pages = book_info['pages']
    print(book_pages)
    return book_pages

show_book_pages(my_book)






# Finally, create at least three new functions that might be useful as we expand our home library app. Perhaps think of a way you could accept additional arguments when the function is called? Also, imagine you have a list filled with dictionaries like above.

# Code below

def sort_book_info_list(book_info_list):
    for book_info in book_info_list:
        print(sort_book_info(book_info))

sort_book_info_list(the_book_list)

def show_set_of_authors(book_info_list):
    author_set = set()

    for book_info in book_info_list:
        author_set.add(book_info["author"])

    return author_set

print(show_set_of_authors(the_book_list))

def show_total_pages(book_info_list):
    total_pages = 0

    for book_info in book_info_list:
        total_pages += book_info["pages"]
    
    return total_pages

print(show_total_pages(the_book_list))