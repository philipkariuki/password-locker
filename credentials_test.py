import unittest
from credentials import Credentials
from user import User


class TestCredentials(unittest.TestCase):
	'''
	Test class that defines test cases for the credentials class behaviours.
	Args:
		unittest.TestCase: helps in creating test cases
	''' 
	def setUp(self):
		'''
		Creates an account's credentials before each test
		'''
		self.new_credential = Credentials('Philip','Twitter','philippo','32541235')

	
	def test__init__(self):
		'''     
		Used to test if the creation of credential instances is executed properly
		'''
		self.assertEqual(self.new_credential.user_name,'Philip')
		self.assertEqual(self.new_credential.site_name,'Twitter')
		self.assertEqual(self.new_credential.account_username,'philippo')
		self.assertEqual(self.new_credential.password,'32541235')

  
	def test_check_user(self):
		'''
		Function to test whether the login in function check_user works as expected
		'''
		self.new_user = User('Philip','Kariuki','philipkariuki@gmail.com','11223344')
		self.new_user.save_user()
		user2 = User('Philip','Kariuki','philipkariuki@gmail.com','11223344')
		user2.save_user()

		for user in User.user_list:
			if user.first_name == user2.first_name and user.password == user2.password:
				current_user = user.first_name
		return current_user

		self.assertEqual(current_user,Credentials.check_user(user2.password,user2.first_name))

		

	def test_save_credentials(self):
		'''
		Checks if new credential is saved into credentials list
		'''
		self.new_credential.save_credentials()
		twitter = Credentials('Pablo','Facebook','paulo','87654321')
		twitter.save_credentials()
		self.assertEqual(len(Credentials.credentials_list),2)


	def tearDown(self):
		'''
		Function to clear the credentials list after every test
		'''
		Credentials.credentials_list = []
		User.user_list = []

	def test_show_credentials(self):
		'''
		Test to check if the display_credentials method, displays the correct credentials.
		'''
		self.new_credential.save_credentials()
		twitter = Credentials('Jane','Twitter','maryjoe','pswd100')
		twitter.save_credentials()
		gmail = Credentials('Jane','Gmail','maryjoe','pswd200')
		gmail.save_credentials()
		self.assertEqual(len(Credentials.show_credentials(twitter.user_name)),2)



	
	
if __name__ == '__main__':
	unittest.main()
