class Credentials:
	"""
		Class that generates new instances of user.
	"""

	credentials_list = [] # Empty user list

	def __init__(self,user_name,site_name,account_username,password):

		# docstring removed for simplicity

			self.user_name = user_name
			self.site_name = site_name
			self.account_username = account_username
			self.password = password

	def save_credentials(self):
		'''
		Function to save user
		'''
		User.credentials_list.append(self)