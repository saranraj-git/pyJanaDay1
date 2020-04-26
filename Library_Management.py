
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

'''
/usr/local/bin/python3.8 /Users/saran/PycharmProjects/pyJanaDay1/Library_Management.py
Enter book name: science
Enter science qty: 4
Enter book name to search: science
science book found in library
Enter book name to remove: maths
maths book not found in library

Process finished with exit code 0

'''