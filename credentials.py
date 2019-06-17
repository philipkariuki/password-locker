import random
import string
from user import User # Importing the user class

class Credentials:
	"""
		Class that generates new instances of user.
	"""

	# defining variables
	credentials_list = [] # Empty credentials list

	user_credentials_list = []  # Empty list of credentials created


	def __init__(self,user_name,site_name,account_username,password):

		# docstring removed for simplicity

			self.user_name = user_name
			self.site_name = site_name
			self.account_username = account_username
			self.password = password



	@classmethod
	def check_user(cls,first_name,password):
		'''
		Checks if name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.user_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user



	def save_credentials(self):
		'''
		Function to save new user credentials
		'''
		User.credentials_list.append(self)




	def genRandomStrongPassword(stringLength=8):
		"""Generate a random string of letters, digits and special characters """
		password_characters = string.ascii_letters + string.digits + string.punctuation
		return ''.join(random.choice(password_characters) for i in range(stringLength))



	@classmethod
	def show_credentials(cls,user_name):
		'''
		Displays list of saved credentials
		'''	
		user_credentials_list = []
		for credential in cls.credentials_list:
			if credential.user_name == user_name:
				user_credentials_list.append(credential)
		return user_credentials_list

	@classmethod
	def delete_credentials(cls, name):
		'''
		deletes an account's saved credentials from the credentials_list.
		'''
		for account in cls.credentials_list:
			if account.account_name == name:
				Credentials.credentials_list.remove(account)

