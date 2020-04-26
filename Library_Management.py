
student = {}
books = {}

def add_books(name,quantity):
    books[name] = quantity

def get_books(name):
    if name in books.keys():
        print("{} book found in library".format(name))
    else:
        print("{} book not found in library".format(name))

def remove_books(name):
    if name in books.keys():
        books.pop(name)

bname = str(input("Enter book name: "))
bqty = int(input("Enter {} qty: ".format(bname)))
add_books(bname, bqty)


search = str(input("Enter book name to search: "))
get_books(search)

rbook = str(input("Enter book name to remove: "))
remove_books(rbook)
get_books(rbook)