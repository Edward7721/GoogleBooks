from unittest import TestCase
from lib import runner
from lib import verify_file_exists
class Test_Book_Search(TestCase):

    """
    TEST console input

    Test1: Search with valid string is saved
    Script: test_search_1
    data_list = ['test.csv', 's', 'new york weather', 'a', 'q' ]
    Step1: 'Please, provide a csv file name to save your search or load >> ' User input: test.csv
    Step2: 'SELECT: Search or Load books library ("S"/"L"), "q" - quit >>' User input: s
    Step3: 'SEARCH: Search string >>' User input: new york weather
    Step4: 'SEARCH: how many items to save (range: [0, 40],  or  "a" -  by default ) >>' User input: a
    Verify:
        1. 'Response Status Code: 200
        2. File test.csv saved in Library folder
        3. File content has headers line and 10 rows with records (By default - 10 results)
    Step5: Sort your books by:
             1 - price
             2 - avg ratings
             3 - rating count
             4 - published date
             5 - page count
             q - quit
        User input: q
    Verify: Process finished with exit code 0
    """
    def test_search_1(self):
        data_list = ['test.csv', 's', 'new york weather', 'a', 'q' ]
        p = runner.cmd_exec('console_input.py', data_list)
        assert (p == 0)
        file_csv = '\\Library\\' + data_list[0]
        assert (verify_file_exists.verify_file_exists(file_csv))
        line_count = verify_file_exists.get_file_line_count('Library\\ + data_list[0]')
        if data_list[3] == 'a': # By default you will get 10 results
            count = 10 + 1
        else:
            count = data_list[3] + 1
        assert (line_count == count)

    """
    Test2: Search result has correct number of records (data driven TC)
    data_list = ['test.csv', 's', 'new york weather', 1 , 'q' ]
    data_list = ['test.csv', 's', 'new york weather', 2 , 'q' ]
       ...
    Test with User inputs: 1, 2, 8, 10, 39, 40
    Execute Step1 - Step3
    Step4: 'SEARCH: how many items to save (range: [0, 40],  or  "a" -  by default ) >>' User input: one from above
    Verify:
        1. 'Response Status Code: 200
        2. File test.csv saved in Library folder
        3. File content has headers and correct number of rows with records

    """
    def test_search_2(self):
        data_list = ['test.csv', 's', 'new york weather', 1, 'q' ]
        p = runner.cmd_exec('console_input.py', data_list)
        assert (p == 0)
        file_csv = '\\Library\\' + data_list[0]
        assert (verify_file_exists.verify_file_exists(file_csv))
        line_count = verify_file_exists.get_file_line_count('Library\\ + data_list[0]')
        if data_list[3] == 'a': # By default you will get 10 results
            count = 10 + 1
        else:
            count = data_list[3] + 1
        assert (line_count == count)
