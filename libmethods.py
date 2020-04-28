student = {}
books = {}

def add_books(name,quantity):
    if get_books(name) == True:
        print("{}x books already in the library, adding {}x more books".format(books[name],quantity))
        books[name] = books[name] + quantity
        print("new count of {} books = {} ".format(name, books[name]))
    elif get_books(name) == False:
        print("{} not found in library so adding fresh books".format(name))
        books[name] = quantity
    else:
        print("unknown error")

def get_books(name):
    if name in books.keys():
        print("{}x {} books found in library".format(books[name], name))
        return True
    else:
        print("{} book not found in library".format(name))
        return False

add_books("maths",4)
add_books("maths",4)

get_books("maths")

remove_books("maths", 2):
    if get_books ==True:
        get the count of the existing books
        subtract existing books with the user provided books count
        overwrite the books with the new value
    elif get_books == False:
        print books does not exist in the library, so no action to take



'''
Before adding the books, check whether any existing book avail in the library
If there are any existing books found in the library then check the count of the existing books
Along with the existing books then add the new books to the count
'''

'''
Before adding a student , check whether the student is already registered in the library
  - If registered already then check how many books he borrowed before
  - If he already borrowed the books before then add the new books count to the existing books count which he borrowed
'''