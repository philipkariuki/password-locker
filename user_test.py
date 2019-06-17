import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

	'''
	Test class that defines test cases for the user class behaviours.

	Args:
	    unittest.TestCase: TestCase class that helps in creating test cases
	'''

	def setUp(self):
		'''
		Set up method to run before each test cases.
		'''
		self.new_contact = User("Philip","Kariuki","philipkariuki@gmail.com","11223344") # create user object

	def test_init(self):
		'''
		test_init test case to test if the object is initialized properly
		'''

		self.assertEqual(self.new_contact.first_name,"Philip")
		self.assertEqual(self.new_contact.last_name,"Kariuki")
		self.assertEqual(self.new_contact.email,"philipkariuki@gmail.com")
		self.assertEqual(self.new_contact.password,"11223344")



	def test_save_user(self):
		'''
		Test to check if the new users info is saved into the users list
		'''
		self.new_user.save_user()
		self.assertEqual(len(User.users_list),1)

if __name__ == '__main__':
	unittest.main()