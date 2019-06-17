# from credentials import Credentials
global users_list

class User:
	"""
		Class that generates new instances of user.
	"""

	user_list = [] # Empty user list

	def __init__(self,first_name,last_name,email,password):

		# docstring removed for simplicity

			self.first_name = first_name
			self.last_name = last_name
			self.email = email
			self.password = password

	def save_user(self):
		'''
		Function to save user
		'''
		User.user_list.append(self)



	@classmethod
	def check_user(cls,first_name,password):
		'''
		Checks if name and password entered match entries in the users_list
		'''
		current_user = ''
		for user in cls.user_list:
			if (user.first_name == first_name and user.password == password):
				current_user = user.first_name
		return current_user



	# def delete_user_credentials(self):
	# 	'''
	# 	delete_user method deletes a saved user from the user_list
	# 	'''
	# 	User.user_user.remove(self)