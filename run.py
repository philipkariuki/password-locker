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
	User.save_user(user)


def verify_user(first_name,password):
	'''
	Checks the existance of a user before creating credentials
	'''
	checks_user = Credentials.check_user(first_name,password)
	return checks_user


def generate_password():

	genPass = Credentials.genRandomStrongPassword()
	return genPass


def create_credential(user_name,site_name,account_username,password):

	new_credential=Credentials(user_name,site_name,account_username,password)
	return new_credential

def save_credential(credential):

	Credentials.save_credentials(credential)


def show_credentials(user_name):
	return Credentials.show_credentials(user_name)
	
def display_users():
   return User.display_users()




# def delete_credentials(cls, name):
# 		'''
# 		deletes an account's saved credentials from the credentials_list.
# 		'''
# 		for account in cls.credentials_list:
# 			if account.account_name == name:
# 				Credentials.credentials_list.remove(account)

# Main
def main():
	print(' ')
	print('=' * 100)
	print("Wilkommen To Password Vault ")
	while True:
		print('='* 100)  
		short_code = input("Use these to navigate: \n nac- create a new user account \n lg - login into your existing account \n dis - show list of created accounts \n qt - exit from password locker \n").lower().strip()
		print('='* 100)
		
		if short_code == "qt":
				print(' ')
				print("Ciao! (^ Q ^)/゛")
				print(' ')
				print ('x' * 100)
				print(' ')
				break
		
		elif short_code == "dis":
				if display_users():
						print("Here's a list of the all the users in our database:")
						print(' ')
						for user in display_users():
								print(f"{user.first_name}")
								print(' ')
				else:
						print(' ')
						print("No users saved yet")
						print(' ')
								
		
		elif short_code == "nac":
				print("Create new Password Vault Account ")
				print('=' * 70)
				first_name = input("First Name: ")
				last_name = input("Last Name: ")
				email = input("Email: ")
				password = input("Password: ")
								
				save_user(create_user(first_name,last_name,email,password))
				print('\n')
				
				print(f"Hi,{first_name} {last_name} your account has been created. Your password is {password}")
				print(' ')
				print('=' * 70)
				
		
				
		elif short_code == 'lg':
			print("="*70)
			print(' ')
			print('Welcome to login. Please insert your account details to continue:')
			user_name = input('First Name - ').strip()
			password = str(input('Login Password - '))
			user_found = verify_user(user_name,password)
			if user_found == user_name:
				print(' ')
				print(f'Welcome {user_name}. Select an option to continue.')
				print(' ')
				while True:
					print("="*70)
					print('Navigation codes: \n cac-Create a new Credential \n dpc-Display Credentials \n back- Exit to main menu')
					short_code = input('Select choice: ').lower().strip()
					print("="*70)
					if short_code == 'back':
						print(" ")
						print(f'You\'ve exited credentials management and returned to the main menu {user_name}')
						break
					elif short_code == 'cac':
						print(' ')
						print('Here you can use our unique world class algorithms to create secure credentials:')
						print(' ')
						print('You can use our cutting-edge password generator to generate uncrackable passwords ;-)')
						print(' ')
						print('Please fill in the fields below')
						site_name = input('Site Name: ').strip()
						account_name = input('Site\'s Account Name: ').strip()
						while True:
							print(' ')
							print("="*70)
							print('Select a choice:(Best to use our password generator) \n yp-enter a password of your choice \n gp-generate a strong password \n cn-cancel')
							selectedPassChoice = input('Choose an option: ').lower().strip()
							print("="*70)
							if selectedPassChoice == 'yp':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif selectedPassChoice == 'gp':
								password = generate_password()
								break
							elif selectedPassChoice == 'cn':
								break
							else:
								print('Wrong short code selected. Use yp gp cn.')
						save_credential(create_credential(user_name,site_name,account_name,password))
						print(' ')
						print(f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
						print(' ')
					elif short_code == 'dpc':
						print(' ')
						if show_credentials(user_name):
							print('Here is a list of all your credentials')
							print(' ')
							for credential in show_credentials(user_name):
								print(f'Site Name: {credential.site_name} - Account Name: {credential.account_username} - Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("No credentials created yet.")
							print(' ')
					
					else:
						print('Wrong option selected. Use the following shortcodes to select a choice \n\n cac/dpc/back')

			else: 
				print('\n')
				print('x' * 100)
				print(' ')
				print('Incorrect login! Please try again!')
				print(' ')		
		
		else:
			print(' ')
			print("Please use a valid short code")
			print(' ')	


if __name__ == '__main__':
	main()
