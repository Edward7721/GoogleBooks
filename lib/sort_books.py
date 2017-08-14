import csv
import datetime
from lib.Books import Books
KEY_SORT = {'price': 'items_saleInfo_retailPrice_amount', 'avg rating': 'items_volumeInfo_averageRating',
            'rating count': 'items_volumeInfo_ratingsCount','published date': 'items_volumeInfo_publishedDate',
            'page count': 'items_volumeInfo_pageCount'}
class SortBooks():

    def __init__(self, file_cvs):
        self.file = file_cvs
        self.__read_books()

    def __read_books(self):
        data = []
        self.books = []
        csv_f = csv.reader(open(self.file, 'rb'))
        for row in csv_f:
            data.append(row)
        self.keys = data[0]
        for i in range(1, len(data)):
            book = Books(self.keys, data[i])
            self.books.append(book)

    def sort_books(self, by_key):
        k = KEY_SORT[by_key]
        print 'Sort by', by_key, k
        if by_key == 'price':
            pass
        elif by_key == 'published date':
            pass
            #sorted(books, key=lambda x: datetime.datetime.strptime(x, '%m-%Y'))
        elif by_key == 'page count':
            self.books.sort(key=lambda x: int(x.getValue(k)), reverse=True)
        else:
            # To sort the list by value k
            self.books.sort(key=lambda x: x.getValue(k), reverse=True)

        # To return a new list, use the sorted() built-in function...
        #newlist = sorted(books, key=lambda x: x.getValue(k))
        for b in self.books:
            print b.getValue(k)
        self.__save_sorted_books()

    def __save_sorted_books(self):
        ofile  = open(self.file, "wb")
        writer = csv.writer(ofile, quoting=csv.QUOTE_ALL)
        writer.writerow(self.keys)
        for book in self.books:
            row = book.data
            writer.writerow(row)
        ofile.close()
