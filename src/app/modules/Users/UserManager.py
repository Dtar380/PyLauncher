########################################
#####  Import Modules/Libs         #####
########################################

##### Built-in Libs                #####
from uuid import uuid5, NAMESPACE_URL
from json import loads, dump
from os.path import exists

##### Internal Modules             #####
from modules.System.SystemFunctions import SystemFunctions
from modules.Users.User import User

########################################
#####  UsersManager                #####
########################################

#####  UserManager Class           #####
class UserManager:

    def __init__(self, users_file):
        self.users_file = users_file # Gets the users.json directory
        self.users = self.load_users() # Loads all users into the variable
        if not self.users: self.create_user(True) # If there are no users create a user

    # Loads the users
    def load_users(self):
        if exists(self.users_file): # If the users file exists

            with open(self.users_file, 'r') as f: # Open the users file
                data = loads(f.read()) # Loads the data from the file
                
                # Returns to User class the parameters from each user
                return [User(inst['username'], inst['uuid'], inst['selected']) for inst in data]
        else:
            print('Error. No users file detected') # Prints an error
            exit() # Exits the code

    # Save the users
    def save_users(self):
        data = [inst.user_dict() for inst in self.users] # Creates a list with all users

        with open(self.users_file, 'w') as f: # Opens the file
            dump(data, f, indent=4, separators=(',',':')) # Dumps the data into the file

    # Create a user
    def create_user(self, selected = None):
        while True: # Infinite loop
            SystemFunctions().clear() # Uses the clear() method form SystemFunctions
            username = input('Select a username: ') # Asks for input

            # Asks for confimation
            confirm_name = input(f'Are you sure you want the name to be {username}? (y/n) ')
            
            if confirm_name.lower() == 'y': # If the confirmation true 
                break # break the loop

        user_uuid = uuid5(NAMESPACE_URL, username) # Creates a uuid for the username
        new_user = User(username, str(user_uuid), selected) # Creates a new object with User class
        self.users.append(new_user) # Appends to the list of users
        self.save_users() # Saves the users into the json

    # Select a user
    def select_user(self, user_id):
        if 0 <= user_id < len(self.users): # Checks if the user exists
            
            # Marks every user as unselected
            for inst in self.users: 
                inst.selected = False

            self.users[user_id].selected = True # Marks the selected user as selected
            self.save_users() # Saves the users into the json

    # Get current selected user
    def get_selected_user(self):
        for i in self.users: # Checks every user
            if i.selected: # If the user is selected

                # Returns the values username and uuid
                return [i.username, i.uuid]

    # Delete a user
    def delete_user(self, user_id):
        if 0 <= user_id < len(self.users): # Checks if user exists

            if self.users[user_id].selected: # Checks if the user is selected
                print('\nUser is selected\n') # Prints an error
                return # Returns with nothing
            
            else:
                del self.users[user_id] # Deletes the user
                
        self.save_users() # Saves the users into the json
