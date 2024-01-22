########################################
#####  Import Modules/Libs         #####
########################################

##### Built-in Libs                #####
from modules.System.SystemFunctions import SystemFunctions

########################################
#####  UsersManager                #####
########################################

#####  User Class                  #####
class User:

    def __init__(self, username, uuid, selected=None):
        self.username = username # Gets the username argument of the User
        self.uuid = uuid # Gets the uuid argument of the User
        self.selected = selected # Gets the selected argument of the User

    # Creates a dictionary with the parameters
    def user_dict(self):
        return {
            "username": self.username,
            "uuid": self.uuid,
            "selected": self.selected
        }
