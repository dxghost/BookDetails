import sqlite3
conn = sqlite3.connect('books.db')
c = conn.cursor()

#Primary Tables
c.execute('''CREATE TABLE CrudeDetails(BookName text not null ,ISBN integer not null ,Publisher text not null ,Price text,Subject text not null ,Author text not null ,IssueYear integer,ImageURL text,Section text,Hall text,Corridor integer,StandNo integer)''')
c.execute('''CREATE TABLE Books(BookName text,ISBN integer PRIMARY KEY ,Price text,IssueYear integer,ImageURL text)''')
c.execute('''CREATE TABLE Publishers(PublisherID integer PRIMARY KEY ,PublisherName text Unique,Section text,Hall text,Corridor text,StandNo text)''')
c.execute('''CREATE TABLE Subjects(SubjectID Integer PRIMARY KEY ,Subject text unique not null  )''')
c.execute('''CREATE TABLE Authors(AuthorID Integer PRIMARY KEY ,AuthorName text UNIQUE not NULL  )''')

#Secondary Tables
c.execute('''CREATE TABLE BookAuthor(book REFERENCES Books(BookName),author REFERENCES Authors(AuthorName),PRIMARY KEY (book,author))''')
c.execute('''CREATE TABLE BookSubject(book REFERENCES Books(BookName),subject REFERENCES Subjects(Subject),PRIMARY KEY (book,subject))''')
c.execute('''CREATE TABLE BookPublisher(book REFERENCES Books(BookName),subject REFERENCES Publishers(PublisherName),PRIMARY KEY (book,subject))''')



#Fill Primary Tables
def FillBooks():
    c.execute("SELECT BookName,ISBN,Price,IssueYear,ImageURL FROM CrudeDetails")
    for pair in c.fetchall():
        c.executemany("insert into Books Values(?,?,?,?,?)", [pair])

def FillPublishers():
    PublisherID = 0
    c.execute("SELECT Publisher,Section,Hall,Corridor,StandNo FROM CrudeDetails")
    for i in c.fetchall():
        attrs = [(PublisherID, i[0], i[1], i[2], i[3], i[4])]
        try:
            c.executemany("insert into Publishers values(?,?,?,?,?,?)", attrs)
            PublisherID += 1
        except:pass

def FillAuthors():
    AuthorID = 0
    c.execute("SELECT Author FROM CrudeDetails")
    for i in c.fetchall():
        if i[0].split(',') == 1:
            attrs = [(AuthorID, i[0])]
            try:
                c.executemany("insert into Authors values(?,?)", attrs)
                AuthorID += 1
            except:pass
        else:
            for j in i[0].split(','):
                attrs = [(AuthorID, j)]
                try:
                    c.executemany("insert into Authors values(?,?)", attrs)
                    AuthorID += 1
                except:pass

def FillSubjects():
    SubjectID = 0
    c.execute("SELECT Subject FROM CrudeDetails")
    for i in c.fetchall():
        if i[0].split(',') == 1:
            attrs = [(SubjectID, i[0])]
            try:
                c.executemany("insert into Subjects values(?,?)", attrs)
                SubjectID += 1
            except:pass
        else:
            for j in i[0].split(','):
                attrs = [(SubjectID, j)]
                try:
                    c.executemany("insert into Subjects values(?,?)", attrs)
                    SubjectID += 1
                except:pass


conn.commit()
conn.close()
