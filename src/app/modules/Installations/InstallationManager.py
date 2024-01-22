########################################
#####  Import Modules/Libs         #####
########################################

##### External Libs                #####
from minecraft_launcher_lib.command import get_minecraft_command as command

##### Built-in Libs                #####
from os.path import exists
from json import loads, dump
from os.path import exists

##### Internal Modules             #####
from modules.System.SystemFunctions import SystemFunctions
from modules.Installations.Installation import Installation

##### Constants                    #####
from modules.constants import launcher_path

########################################
#####  InstallationManager         #####
########################################

#####  InstallationManager Class   #####
class InstallationManager:

    def __init__(self, installations_file):
        self.installations_file = installations_file # Gets the installations.json directory
        self.installations = self.load_installations() # Loads all installations into the variable

    # Loads the installations
    def load_installations(self):
        if exists(self.installations_file): # If the installations file exists

            with open(self.installations_file, 'r') as f: # Open the installations file
                data = loads(f.read()) # Loads the data from the file

                # Returns to Installation class the parameters from each installation
                return [Installation(inst['name'], inst['gameDir'], inst['versionId'], inst['memoryMax'], inst['custom']) for inst in data]
        else:
            print('Error. No Installation file detected') # Prints an error
            exit() # Exits the code

    # Save the installations
    def save_installations(self):
        data = [inst.installation_dict() for inst in self.installations] # Creates a list with all installations

        with open(self.installations_file, 'w') as f: # Opens the file
            dump(data, f, indent=4, separators=(',',':')) # Dumps the data into the file

    # Create an installation
    def create_installation(self, name, gameDir, versionId, MaxRamArg):
        new_installation = Installation(name, gameDir, versionId, MaxRamArg, True) # Creates a new object with Installation class
        self.installations.append(new_installation) # Appends to the list of installations
        self.save_installations() # Saves the installations into the json file

    # Execute an installation
    def execute_installation(self, installation_id, username, uuid):
        if 0 <= installation_id < len(self.installations): # Checks that the installation exists

            # Runs the installation calling the method execute_installation of Installations class
            self.installations[installation_id].execute_installation(username, uuid)

    # Change the parameters of an installation
    def change_parameters(self, installation_id, name=None, gameDir=None, versionId=None, MaxRamArg=None):
        if 0 <= installation_id < len(self.installations): # Checks that the installation exists

            if name is not None: # If there was given a value for name
                # Change the current value name of the selected installation for the new one
                self.installations[installation_id].name = name

            if gameDir is not None: # If there was given a value for gameDir
                # Change the current value gameDir of the selected installation for the new one
                self.installations[installation_id].gameDir = gameDir

            if versionId is not None: # If there was given a value for versionId
                # Change the current value versionId of the selected installation for the new one
                self.installations[installation_id].versionId = versionId

            if MaxRamArg is not None: # If there was given a value for MaxRamArg
                # Change the current value MaxRamArg of the selected installation for the new one
                self.installations[installation_id].MaxRamArg = MaxRamArg

            self.save_installations() # Save the installation into the json file

    # Opens the folder of the installation
    def open_installation_path(self, installation_id):
        if 0 <= installation_id < len(self.installations): # Checks that the installation exists
            # Calls the method open_file_explorer of the class SystemFunctions
            SystemFunctions().open_file_explorer(self.installations[installation_id].gameDir)

    # Delete an installation
    def delete_installation(self, installation_id):
        if 0 <= installation_id < len(self.installations): # Checks that the installation exists
            del self.installations[installation_id] # Deletes the selected installation

        self.save_installations() # Saves the installations into the json file
