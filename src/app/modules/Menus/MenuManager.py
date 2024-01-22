########################################
#####  Import Modules/Libs         #####
########################################

##### Internal Modules             #####
from modules.System.SystemFunctions import SystemFunctions

########################################
#####  MenusManager                #####
########################################

#####  MenuManager class           #####
class MenuManager:

    def __init__(self, actions):
        self.actions = actions # Gets the actions argument of the Menu

    # Prints the selection menu
    def print_menu(self, string):
        while True: # Infinite loop
            SystemFunctions().clear() # Clears the consol

            print(string) # Prints the string argument

            for i, variable in enumerate(self.actions):
                print(f'▐{variable} {i + 1}') # Prints each action and its index
            selection = input('\n') # Asks for input

            try:
                index = int(selection) - 1 # Transform selection into an ineteger and subtract 1
                if 0 <= index < len(self.actions): # Check if the action exists
                    return index # Returns the index of the action
                
                else:
                    print('\nInvalid selection\n') # Prints an error

            except ValueError:
                print('\nInvalid selection\n') # Prints an error
