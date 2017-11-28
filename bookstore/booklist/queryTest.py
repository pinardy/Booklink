from query import *
import unittest

print('************************** Start of test for query.py **************************')

"""
class Test(unittest.TestCase):
	
	def setUp(self):
		pass
	
	def test_retrieve_profile_1(self):
		self.assertTrue(retrieveProfile('eiros'))

	def test_retrieve_profile_2(self):
		self.assertFalse(retrieveProfile('eiross'))
	
	
		
if __name__ == '__main__':
	unittest.main()
"""

#if (bool(getBook('eiros')==None)):
#	print('hey')
#else:
#	print('right!')

#print(getAllBooks())
#getBook('eiros')
#retrieveProfile('eiros')
#feedbackBook('eiros','9780132943260','2012-01-01',1,'hi')
#print(getFeedbackHistory('eiros'))
#print(bookRating('9780132943260'))

#insertBook('DB','hardcover',50,'Timmy Turner','CRC Press',2000,1,'1234567890','1234567890123',5)
#print(getAllBooks())
#deleteBook('1234567890123')
#print(getAllBooks())
getInventory('1234567890123')

#print(getInventory('9780132943260')[0][0])
#print(userRating('eiros'))
#print(bookRating('9780132943260'))