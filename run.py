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