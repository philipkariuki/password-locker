import random
import string

class Credentials:
	"""
		Class that generates new instances of user.
	"""

	credentials_list = [] # Empty credentials list

	def __init__(self,user_name,site_name,account_username,password):

		# docstring removed for simplicity

			self.user_name = user_name
			self.site_name = site_name
			self.account_username = account_username
			self.password = password

	def save_credentials(self):
		'''
		Function to save new user credentials
		'''
		User.credentials_list.append(self)


	def show_credentials


	def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
		'''
		Function to generate an 8 character password for a credential
		'''
		gen_pass=''.join(random.choice(char) for _ in range(size))
		return gen_pass


	def randomStrongPassword(stringLength=8):
    """Generate a random string of letters, digits and special characters """
    password_characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(password_characters) for i in range(stringLength))

