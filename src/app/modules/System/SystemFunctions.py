########################################
#####  Import Modules/Libs         #####
########################################

##### Built-in Libs                #####
from time import sleep
from subprocess import Popen
from os import system as execute
from platform import system as sys
from urllib import error, request

########################################
#####  System Functions            #####
########################################
class SystemFunctions:

    def __init__(self):
        self.os = sys() # Gets the operatinf system
        self.check_os_compatibility() # Check if the os is compatible with the program

    # Checks if the os is Windos, MacOS or Linux
    def check_os_compatibility(self):
        if self.os == 'Windows' or self.os == 'Darwin' or self.os == 'Linux':
            pass
        else:
            print('\nSystem not compatible\n\n Exiting program')
            sleep(1)
            exit()

    # Checks if user has internet connection
    def get_internetConnection(self):
        try:
            request.urlopen('https://www.google.com', timeout=1) # Tries connecting to the google servers
            return True # Returns True
        
        except error.URLError: # Except user has no connection
            return False # Returns False

    # Clear the consol after specified time
    def clear(self, time = 1):
        sleep(time) # Stop the program 1 second
        execute('cls' if self.os == 'Windows' else 'clear') # Clear the consol

    # Opens a file on the file explorer
    def open_file_explorer(self, path):
        if self.os == 'Windows': # If the OS is windows execute this command
            Popen(['explorer', '/select,', path]) # Open the path on the file explorer

        elif self.os == 'Darwin': # If the OS is MacOS execute this command
            Popen(['open', '--', path]) # Open the path on the file explorer

        elif self.os == 'Linux': # If the OS is linux execute this command
            Popen(['xdg-open', path]) # Open the path on the file explorer
