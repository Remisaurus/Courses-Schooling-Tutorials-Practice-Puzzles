# import unittest

# class Testsum(unittest.TestCase):
    
#     def test_sum(self):
#         self.assertEqual(sum([1,2,3]), 6, 'should be six')

"""import unittest

class Testbigvalue(unittest.TestCase):
    def test_large_numbers(self):
        self.assertEqual(max([1,2,3,4,5,6,7]), 7)
        self.assertEqual(max([-809, -99, -9]), -9)
        self.assertEqual(max([1869247926, 10**35]), 10**35)
       
if __name__ == '__main__':
    unittest.main()"""
    
# def make_list(filename):
#     checklist = []
#     try:
#         with open(filename, 'r') as boss:
#             for row in boss:
#                 checklist.append(row)
#             print('file loaded.')
#     except:
#             print('an error ensued during loading the file. manually check if it exists.')
#     return checklist
     
# def check_for_list(check_this_list, andthisfile):
#     listline = 0
#     for each in check_this_list:  
#         listline += 1  
#         fileline = 0    
#         try:
#             with open(andthisfile, 'r') as boss:
#                 for row in boss:
#                     fileline += 1
#                     if each in row:
#                         print(f'found similarity! listnumber {listline} and filelinenumber: {fileline}')
#         except:
#             print('an error ensued during loading the file. manually check if it exists.')
    
# if __name__ == '__main__':
#     check_for_list(make_list('test_data.txt'), 'test_data.txt')

import unittest

class Testunevenlist(unittest.TestCase):
    def test_uneven_numbers(self):
        self.assertEqual(return_odd_numbers([-3,-2,-1,0,1,2,3]), [-3,-1,1,3])
        self.assertEqual(return_odd_numbers([3,2,1,0,-1,-2,-3]), [-3,-1,1,3])
        self.assertEqual(return_odd_numbers_reversed([-3,-2,-1,0,1,2,3]), [3,1,-1,-3])
        self.assertEqual(return_odd_numbers_reversed([3,2,1,0,-1,-2,-3]), [3,1,-1,-3])

    
def return_odd_numbers(input_list):
    even_numbers = []
    uneven_numbers = []
    for all in input_list:
        if all == 0:
            even_numbers.append(all)
        elif all % 2 == 0:
            even_numbers.append(all)
        else:
            uneven_numbers.append(all)
    return sorted(uneven_numbers)

def return_odd_numbers_reversed(input_list):
    even_numbers = []
    uneven_numbers = []
    for all in input_list:
        if all == 0:
            even_numbers.append(all)
        elif all % 2 == 0:
            even_numbers.append(all)
        else:
            uneven_numbers.append(all)
    return sorted(uneven_numbers, reverse=True)
       
if __name__ == '__main__':
    unittest.main()