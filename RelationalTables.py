import sqlite3
conn = sqlite3.connect('books.db')
c = conn.cursor()

def Fill_BookAuthor():
    c.execute("SELECT  BookName,Author From CrudeDetails")
    result=c.fetchall()
    for pair in result:
        if len(pair[1].split(','))==1:
            if pair[1] != '-':
                try:
                    c.executemany("insert Into BookAuthor Values(?,?)",[pair])
                except:pass
        else:
            for j in pair[1].split(','):
                try:
                    c.executemany("insert into BookAuthor Values(?,?)",[(pair[0],j)])
                except:pass
def Fill_BookSubject():
    c.execute("SELECT  BookName,Subject From CrudeDetails")
    result=c.fetchall()
    for pair in result:
        if len(pair[1].split(','))==1:
            if pair[1] != '-':
                try:
                    c.executemany("insert Into BookSubject Values(?,?)",[pair])
                except:pass
        else:
            for j in pair[1].split(','):
                try:
                    c.executemany("insert into BookSubject Values(?,?)",[(pair[0],j)])
                except:pass
def Fill_BookPublisher():
    c.execute("SELECT  BookName,Publisher From CrudeDetails")
    result=c.fetchall()
    for pair in result:
        if pair[1] != '-':
            try:
                c.executemany("insert Into BookPublisher Values(?,?)",[pair])
            except:pass

conn.commit()
conn.close()
