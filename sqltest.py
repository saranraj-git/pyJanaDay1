import sqlite3

conn = sqlite3.connect('libmgmt.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS books(bookid integer NOT NULL,bookname varchar(20) not null,bookquantity integer not null)")
c.execute("CREATE TABLE IF NOT EXISTS student(studentid integer NOT NULL,studentname varchar(20) not null)")

def addbooks(ab_books_name,ab_books_qty):
    bookid = 1
    query = "INSERT INTO books values({},'{}',{})".format(bookid,ab_books_name,ab_books_qty)
    bookid += 1
    c.execute(query)

def getbooks(gb_bookname):
    gbquery = "select * from books where bookname = '{}'".format(gb_bookname)
    c.execute(gbquery)
    outbookid, outbookname, outbookqty = c.fetchone()
    print("From Database - book id is {} ".format(outbookid))
    print("From Database - book name is {} ".format(outbookname))
    print("From Database - book qty is {} ".format(outbookqty))

usr_bookname = str(input("Enter the book name : "))
usr_bookqty = int(input("Enter the book qty : "))
#addbooks(usr_bookname,usr_bookqty)
getbooks(usr_bookname)

conn.commit()
conn.close()

