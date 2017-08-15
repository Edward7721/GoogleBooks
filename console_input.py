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
from lib import data_strings
from lib import verify_file_exists

def main():
    Str = data_strings
    print Str.SCRIPT_HEADER
    sort_str = Str.sort_str
    SORT_KEY = Str.SORT_KEY
    value = ''
    booksAPI = Api()
    # Get input.
    print 'Note: all files will be saved or loaded into/from <Library> folder\n'
    while value != "q":
        value = raw_input('Please, provide a csv file name to save your search or load >> ')
        csv_file = 'Library\\' + value
        value = raw_input('\nSELECT: Search or Load books library ("S"/"L"), "q" - quit >>').lower()
        if value == "q":
            break
        if value not in ['s', 'l']:
            continue
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
            result, status = booksAPI.get(q=q, maxResults=maxResults)
            # Save the search result
            if  status== 200:
                coverter.conv(csv_file, json_value = result)
        elif value == "l":
            if not verify_file_exists.verify_file_exists('\\' + csv_file):
                continue

        value = raw_input('\nSort your books by:\n' + sort_str + '>>').lower()
        if value.isdigit() and (int(value)>0 and int(value)<6):
            sort_id = value
            books_list = SortBooks(csv_file)
            books_list.sort_books(SORT_KEY[sort_id])
        break
    # Exit message.
    print("Exit")

if __name__ == '__main__':
    main()
      
      
