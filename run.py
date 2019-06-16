from user import User # Importing the user class
from credentials import Credentials # Importing credentials class

def create_user(first_name,last_name,email,password):
	"""
	Function to create new user
	"""

	new_user = new User(first_name,last_name,email,password)
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
	checks_user = Credential.check_user(first_name,password)
	return checks_user


def generate_password():

	gen_pass = Credential.genRandomStrongPassword()
	return gen_pass

