import unittest # Importing the unittest module
from user import User # Importing the contact class

class TestUser(unittest.TestCase):

	'''
	Test class that defines test cases for the user class behaviours.

	Args:
	    unittest.TestCase: class that helps in creating test cases
	'''

	def setUp(self):
		'''
		To test creating a new user account
		'''
		self.new_contact = User("Philip","Kariuki","philipkariuki@gmail.com","11223344") # create user object

	def test_init(self):
		'''
		Used to test if the creation of user instances is executed properly
		'''

		self.assertEqual(self.new_contact.first_name,"Philip")
		self.assertEqual(self.new_contact.last_name,"Kariuki")
		self.assertEqual(self.new_contact.email,"philipkariuki@gmail.com")
		self.assertEqual(self.new_contact.password,"11223344")



	def test_save_user(self):
		'''
		Test whether new users info is saved into user_list
		'''
		self.new_contact.save_user()
		self.assertEqual(len(User.user_list),1)

if __name__ == '__main__':
	unittest.main()