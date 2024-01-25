########################################
#####  Import Modules/Libs         #####
########################################

##### External Libs                #####
from minecraft_launcher_lib.command import get_minecraft_command as command

##### Built-in Libs                #####
from subprocess import run

##### Constants                    #####
from modules.constants import launcher_path

########################################
#####  Installations               #####
########################################

#####  Installation class          #####
class Installation:

    def __init__(self, name, gameDir, versionId, MaxRamArg, type):
        self.name = name # Gets the name argument of the Installation
        self.gameDir = gameDir # Gets the path argument of the Installation
        self.versionId = versionId # Gets the version argument of the Installation
        self.MaxRamArg = MaxRamArg # Gets the memoryMax argument of the Installation
        self.type = type # Gets the type argument of the Installation

    # Executes the instalation
    def execute_installation(self, username, uuid):
        options = { # Creates the options for running the installation
            'username': username, # Gets the username
            'uuid': uuid, # Gets the uuid

            "launcherVersion": "0.2", # Sets the launcher version
            "gameDirectory": self.gameDir, # Sets the files path
            "jvmArguments": [f'-Xmx{self.MaxRamArg}G','-Xms1G'], # Sets max and min RAM
            "disableMultiplayer": False # Enables the multiplayer
        }
        run(command(self.versionId, launcher_path, options)) # Runs the minecraft version

    # Creates a dictionary with the parameters
    def installation_dict(self):
        return {
        "name":  self.name,
        "gameDir": self.gameDir,
        "versionId": self.versionId,
        "memoryMax": self.MaxRamArg,
        "custom": self.type
        }
