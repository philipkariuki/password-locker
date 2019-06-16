import random
import string

class Credentials:
	"""
		Class that generates new instances of user.
	"""

# defining variables
	credentials_list = [] # Empty credentials list

	


def __init__(self,user_name,site_name,account_username,password):

	# docstring removed for simplicity

		self.user_name = user_name
		self.site_name = site_name
		self.account_username = account_username
		self.password = password



@classmethod
	def check_user(cls,first_name,password):
		'''
		Method that checks if the name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in User.users_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user



def save_credentials(self):
	'''
	Function to save new user credentials
	'''
	User.credentials_list.append(self)




def randomStrongPassword(stringLength=8):
  """Generate a random string of letters, digits and special characters """
  password_characters = string.ascii_letters + string.digits + string.punctuation
  return ''.join(random.choice(password_characters) for i in range(stringLength))

