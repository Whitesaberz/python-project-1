### Step 1 - Lists ###

# Fill in this list with several authors you are a fan of. At least 7 or 8 should do.
my_authors = ['J. R. R. Tolkien', 'George R. R. Martin', 'Stephen King', 'Mark Twain', 'George Orwell', 'Jane Austen', 'Agatha Christie','Shakespeare' ]

# Now let's add a new author to the end with the .append() method. Type your code below.

# Code here
# Example: my_authors.append("H.G. Wells")
my_authors.append('H.G. Wells')
print(my_authors)


# Now let's remove an element in the list

# Code here
# Example: my_authors.remove("H.G. Wells")
my_authors.remove('Agatha Christie')
print(my_authors)

# Now access an element by it's index. (Remember it indexes start at 0.)

# Code here
# Example: my_authors[2]
print(my_authors[4])

# Now slice the list.

# Code here
# Example: my_authors[1:4]
print(my_authors[3:7])

### Step 2 - Tuples ###

# Create your tuple below. Assign it to a variable name you can reference later in the exercise.

# Code here
# Example: my_author_tuple = ("F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury")
author_tuple = ('Sally Rooney','Alan Moore', 'Stan Lee' )
print(author_tuple)

### Step 3 - Sets ###

# Create a set with your authors.

# Code here
# Example: my_author_set = {"F. Scott Fitzgerald", "J.K. Rowling", "Ernest Hemingway", "Emily Dickenson", "George Orwell", "Ray Bradbury"}
author_set = {'J. R. R. Tolkien', 'George R. R. Martin', 'Stephen King', 'Mark Twain', 'George Orwell', 'Jane Austen', 'Agatha Christie','Shakespeare'}

# Add a new author to your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
author_set.add('Alan Moore')
print(author_set)
# Try adding the same author again, and be sure to print your set.

# Code here
# Example: my_author_set.add("J.R.R. Tolkien")
author_set.add('Alan Moore')
print(author_set)


### Step 4 - For Loops ###

# Create a for-loop for each of the data-structures above.

# Code here
# Example:

for book in my_authors:
    print(book)

for book in author_tuple:
    print(book)

for book in author_set:
    print(book)

