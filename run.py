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

	genPass = Credentials.genRandomStrongPassword()
	return genPass


def create_credential(user_name,site_name,account_user_name,password):

	new_credential=Credentials(user_name,site_name,account_user_name,password)
	return new_credential

def save_credential(credential):

	Credentials.save_credentials(credential)


def show_credentials(user_name):
	return Credentials.show_credentials(user_name)
	
def display_users():
   return User.display_users()



# Main
def main():
	print(' ')
	print("Wilkommen To Password Locker ")
	while True:
		print('='* 100)  
		short_code = input("Use these to navigate: nac- create a new user account, lg - login into your existing account, dis - show list of created accounts, qt - exit from password locker \n").lower().strip()
		print('='* 100)
		
		if short_code == "qt":
				print("Ciao! (^ Q ^)/゛ ")
				print ('x' * 100)
				break
		
		elif short_code == "nac":
				print("Sign Up")
				print('=' * 30)
				user_name = input("User Name: ")
				password = input("Password: ")
				account_username =input("Account Username: ")
				email = input("Email: ")
				
				save_user(create_user(user_name,password,account_username,email))
				print('\n')
				
				print(f"Hello,{user_name} your account has been created. Your password is {password}")
				print('\n')
				print('=' * 30)
				
			
		else:
			print("Please use a valid short code")


if __name__ == '__main__':
	main()