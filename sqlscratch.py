import sqlite3

conn = sqlite3.connect('sqltest.db')
c = conn.cursor()
#c.execute("CREATE TABLE IF NOT EXISTS books(bookid integer NOT NULL,bookname varchar(20) not null,bookquantity integer not null)")
'''
c.execute("INSERT INTO books values(1,'maths',40)")
c.execute("INSERT INTO books values(2,'science',50)")
c.execute("INSERT INTO books values(3,'geo',30)")

'''

c.execute("select * from books;")
print(c.fetchall())
conn.commit()
conn.close()

def get_books(cbookname):
    c.execute("select * from books;")
    flag = 0
    for fbookid, fbookname, fbookqty in c.fetchall():
        if fbookname == cbookname:
            print("{} {} {}".format(fbookid,fbookname,fbookqty))
            flag = 1

    if flag == 0:
        print("book {} not found".format(cbookname))

    conn.commit()
    conn.close()

#def update_books():

#userbook = str(input("Enter book name to search: "))
#get_books(userbook)
