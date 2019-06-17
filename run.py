from user import User # Importing the user class
from credentials import Credentials # Importing credentials class

def create_user(first_name,last_name,email,password):
	"""
	Function to create new user
	"""

	new_user = User(first_name,last_name,email,password)
	return new_user

def save_user(user):
	'''
	Function to save user
	'''
	user.save_user()


def userVerify(first_name,password):
	'''
	Checks the existance of a user before creating credentials
	'''
	checks_user = Credentials.check_user(first_name,password)
	return checks_user


def generate_password():

	gen_pass = Credentials.genRandomStrongPassword()
	return gen_pass


def create_credential(user_name,site_name,account_user_name,password):

	new_credential=Credentials(user_name,site_name,account_user_name,password)
	return new_credential

def save_credential(credential):

	Credentials.save_credentials(credential)


def show_credentials(user_name):
	return Credentials.show_credentials(user_name)
