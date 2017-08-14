"""
Objective:
==========
The objective of this assignment is to build a console line application with the data that you get from the google books api.
We will be using a simple unauthenticated google books api to get a list of books. And build a library with these books.
Please adhere to good coding practices and code quality.

API:
===
Go ahead and copy paste this link https://www.googleapis.com/books/v1/volumes?q=python on any web browser and see what it returns.
This API can also take additional parameter like https://www.googleapis.com/books/v1/volumes?q=python&maxResults=40
More information about the API can be found here https://developers.google.com/books/docs/v1/reference/volumes/list or by just googling in general.

Requirements:
============
1. The console line app should prompt the user for a search string and based on the input string the app must
   build the library. Please stick to popular search strings like 'dogs','cats','New York'... etc.
2. The app user must be able to save and persist the book/library data in csv file format.
3. Ability to at least sort the books by price, avg rating, rating count, published date, page count
4. The app should be able to save to and load from a csv file.
5. Bonus points for additional interesting and creative features not listed here. (Nice to see, but not required)

Tests:
============
Please include tests to cover your work.
"""

from lib.getBooksJson import Api
from lib import coverter
from lib.sort_books import SortBooks


SCRIPT_HEADER = """
******************************************************************
*                                                                *
*               Books Search Application                         *
*                                                                *
******************************************************************

"""
TEMP_CSV = 'temp\\temp.csv'

def main():
    print SCRIPT_HEADER
    sort_str = """         1 - price
         2 - avg ratings
         3 - rating count
         4 - published date
         5 - page count
         q - quit\n
    """
    SORT_KEY = {'1':'price', '2': 'avg rating', '3': 'rating count', '4':'published date', '5': 'page count'}
    csv_file = TEMP_CSV
    value = ''
    booksAPI = Api()
    while value != "q":
        # Get input.
        value = raw_input('SELECT: Search or Load books library ("S"/"L"), "q" - quit >>').lower()
        if value == "s":
            value = raw_input('SEARCH: Search string >>').lower()
            print("\nBy default you will get 10 or less results")
            q = value
            value = raw_input('SEARCH: how many items to save (range: [0, 40],  or  "a" -  by default ) >>').lower()
            maxResults = None
            if value.isdigit() and int(value)>0:
                maxResults = int(value)
                if  maxResults>40:
                    maxResults = 40
            result = booksAPI.get(q=q, maxResults=maxResults)
            if result:
                value = raw_input('To save csv File provide filepath >>').lower()
                csv_file = value
                coverter.conv(value, json_value = result)
        elif value == "l":
            csv_file = raw_input('To load csv file provide filepath >>').lower()
        elif value == "q":
            break
        else:
            continue
        value = raw_input('Sort your books by:\n' + sort_str + '>>').lower()
        if value.isdigit() and (int(value)>0 and int(value)<6):
            sort_id = value
            books_list = SortBooks(csv_file)
            books_list.sort_books(SORT_KEY[sort_id])

    # Exit message.
    print("You quit.")

if __name__ == '__main__':
    main()