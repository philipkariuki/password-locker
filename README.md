# Password Locker

IP for MC18 week 1 of Python that requires creating a password locker Python module.


#### By **Philip Kariuki**
## Description
##### Week 1 independent project for Moringa Core 18.
The project requires creating a password locker Python module run from Python cli that enables users to create,store and lock their passwords within the module.
#### User Stories
* As a user, I want to create a password locker account with my details, a login username and password.
* As a user, I want to store my already existing account credentials in the application. Assuming I already have a twitter account, I want to store my already existing twitter username and password in the application.
* As a user, I want to create new account credentials in the application.
* As a user, I want the application to generate a strong password for me.
* As a user, I want to have the option of putting in a password that I want to use for the new credential account instead of having the application generate a password for me.
* As a user, I also want to view my various account credentials and their passwords in the application.
## BDD
| Behaviour | Input | Output |
| ------------ |:----------:| -------: | 
| Show short codes for navigation | in your cli run "py run.py"| Shows navigation short codes nac lg qt dis |
| Display existing users|  dis |  Shows list of existing users | 
| Exit application|qt |Exits the module |
| Creating new account | nac| Creates a new account with the parameters:First name,Last name,Email, Password|
| Short code for login|lg  |Enter First name:, Enter Password |
| Create new credential | cac  | Enter Site name:, Enter Account name:, Select yp or gp|
| Enter an existing password | yp  | User enters an existing password|
| Generate strong password | gp  | Application generates a strong passowrd|
| Display existing credentials | dpc  | Shows list of existing credentials for user|
| Exit credentials management | back  | Exists credentials management menu|


## Setup/Installation Requirements
* Python 3.6

To clone this repo, open terminal in your desired folder then run:

        $ git clone https://github.com/philipkariuki/password-locker/

To run the Python application within the folder from your cli:

        $ py run.py
## Known Bugs
No bugs at the moment.
## Languages Used
Python 3.6
## Contributors
<a href="https://github.com/philipkariuki">philipkariuki</a>

## [License](https://github.com/philipkariuki/password-locker/blob/master/LICENSE)
MIT © 2019 [philipkariuki](https://github.com/philipkariuki)
