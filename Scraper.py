import scrapy,sqlite3,win32api


class QuotesSpider(scrapy.Spider):
    name = "crawler"
    start_urls = []
    for i in range(1, 36137 ):
        start_urls.append('https://tibf.ir/en/book?author.searchType=contains&page=%i&translator.searchType=contains&title.searchType=contains&bookLang=fa&publisherOrDistributor.searchType=contains&subject.searchType=contains' %(i))


    def parse(self, response):
        for i in range(1,11):
            #book
            BookName = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > h1:nth-child(1) > a:nth-child(1)::text'%(i)).extract_first()
            ISBN = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > span:nth-child(2)::text'%(i)).extract_first()
            Publisher = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3) > span:nth-child(2)::text'%(i)).extract_first()
            Price = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > span:nth-child(2)::text'%(i)).extract_first().split('\n')[1][8:]
            Subject = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(2) > div:nth-child(6) > span:nth-child(2)::text'%(i)).extract_first()
            Author = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > span:nth-child(2)::text'%(i)).extract_first()
            IssueYear = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(2) > div:nth-child(5) > span:nth-child(2)::text'%(i)).extract_first()
            ImageURL = response.css('div.item-detail:nth-child(%i) > div:nth-child(1) > img:nth-child(1)::attr(src)'%(i)).extract_first()
            #Location
            Section = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(4) > div:nth-child(1) > span:nth-child(2)::text'%(i)).extract_first()
            Hall = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > span:nth-child(2)::text'%(i)).extract_first()
            Corridor = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(4) > div:nth-child(3) > span:nth-child(2)::text'%(i)).extract_first()
            StandNo = response.css('div.item-detail:nth-child(%i) > div:nth-child(2) > div:nth-child(4) > div:nth-child(4) > span:nth-child(2)::text'%(i)).extract_first()
            #Object
            e=Book(BookName,ISBN,Publisher,Price,Subject,Author,IssueYear,ImageURL,Section,Hall,Corridor,StandNo)


class Book:
    def __init__(self,Name,ISBN,Publisher,Price,Subject,Author,IssueYear,ImageURL,Section,Hall,Corridor,StandNo):
        conn = sqlite3.connect('books.db')
        c = conn.cursor()

        self.Name = Name
        self.ISBN = ISBN
        self.Publisher = Publisher
        self.Price = Price
        self.Subject = Subject
        self.Author=Author
        self.IssueYear = IssueYear
        self.ImageURL= ImageURL
        self.Section = Section
        self.Hall = Hall
        self.Corridor = Corridor
        self.StandNo = StandNo

        self.Attrs = [(self.Name,self.ISBN,self.Publisher,self.Price,self.Subject,self.Author,self.IssueYear,self.ImageURL,self.Section,self.Hall,self.Corridor,self.StandNo)]
        c.executemany('INSERT INTO CrudeDetails VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', self.Attrs)
        conn.commit()
        conn.close()

        #self.show()

    def show(self):
        print('\n\n*******************************************************************')
        print('Book Name :  '+ str(self.Name))
        print('Book ISBN :  '+ str(self.ISBN))
        print('Book Publisher :  '+ str(self.Publisher))
        print('Book Price :  '+ str(self.Price))
        print('Book Subject :  '+ str(self.Subject))
        print('Book Author :  '+ str(self.Author))
        print('Book Issue Year :  '+ str(self.IssueYear))
        print('Book Image URL :'+ str(self.ImageURL))
        print('Publisher Section :'+ str(self.Section))
        print('Publisher Hall  :'+ str(self.Hall))
        print('Publisher Corridor :'+ str(self.Corridor))
        print('Publisher StandNo :'+ str(self.StandNo))
        print('*******************************************************************\n\n')



