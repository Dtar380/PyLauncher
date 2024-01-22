########################################
#####  Import Modules/Libs         #####
########################################

##### External Libs                #####
from minecraft_launcher_lib import fabric, quilt

##### Built-in Libs                #####
from os.path import exists
from modules.System.SystemFunctions import SystemFunctions

##### Constants                    #####
from modules.constants import launcher_path

########################################
#####  System Functions            #####
########################################
class InstallationParameters:

    def __init__(self, forced = None, mc_loader = None, version_to_install = None):
        self.forced = forced # Gets the forced state (bool)
        self.mc_loader = mc_loader # Gets the mc_loader being used for the installation proccess
        self.version_to_install = version_to_install # Gets the version that is being installed
        if forced or forced == False: # Checks if the forced conditions is True or False or None
            self.parameters = self.InstallationParametersMenu() # Stablishes the parameters menu state

    # Defines InstallatioParameterMenu function
    def InstallationParametersMenu(self):
        if self.forced: # If the menu is forced
            name = self.get_name() # Make user create a name

            gameDir = self.ask_for_parameters( # Ask the user if want custom path
                'Want to change the directory (y/n) ', # Give the prompt argument
                self.get_gameDir # Give the next function to be executed
            )
            MaxRamArg = self.ask_for_parameters( # Ask the user if want custom ram ammount
                'Want to change max ram? (y/n) ', # Give the prompt argument
                self.get_MaxRamArg # Give the next function to be executed
            )
            versionId = self.get_versionId() # Get the versionId of the installed version folder

            if not gameDir: # If user didnt specified directory
                gameDir = launcher_path # Predetermined directory

            if not MaxRamArg: # If user didnt specified ram amount
                MaxRamArg = 4 # Predetermined ram amount

        else: # If the menu isnt forced
            name = self.ask_for_parameters( # Ask the user if want to change the name
                'Want to change the name? (y/n) ', # Give the prompt argument
                self.get_name # Give the next function to be executed
            )
            gameDir = self.ask_for_parameters( # Ask the user if want to change the path
                'Want to change the directory (y/n) ', # Give the prompt argument
                self.get_gameDir # Give the next function to be executed
            )
            MaxRamArg = self.ask_for_parameters( # Ask the user if want to change the ram ammount
                'Want to change max ram? (y/n) ', # Give the prompt argument
                self.get_MaxRamArg # Give the next function to be executed
            )
            versionId = None # Version Id is None

        return [name, gameDir, versionId, MaxRamArg] # Return the 4 parameters

    # Defines ask_for_parameters function
    def ask_for_parameters(self, prompt, func):
        while True: # Infinite Loop
            SystemFunctions().clear() # Clears the consol

            confirm = input(prompt) # Asks for confimation

            if confirm.lower() == 'y': # If user answers Yes
                return func() # Runs the function specified

            elif confirm.lower() == 'n': # If user answers No
                return None # Returns the vaule None

    # Defines get_user_input function
    def get_user_input(self,prompt_1, prompt_2, try_true = None):
        while True: # Infinite Loop
            SystemFunctions().clear() # Clears the consol

            self.variable = input(prompt_1) # Changes the self.variable to the input

            if self.variable: # If theres an input
                confirm = self.confirm_user_input(prompt_2, try_true) # Gets the value returned from confirm_user_input()

                if confirm.lower() == 'y': # Checks if the value is Yes
                    return self.variable # Returns self.variable

            else: # Else
                ('\nInvalid Input\n') # Prints an invalid input error

    # Defines confirm_user_input function
    def confirm_user_input(self, prompt, try_true = None):
        if try_true: # If try_true is True

            try:
                self.variable = int(self.variable) # Integer self.variable
                try_true = False # Set try_tru to False

            except ValueError: # If value error arraises
                print('Ram especified not integer') # Prints an error message
                return None # Returns None

        if not try_true: # If try_true is False
            prompt[1] = str(self.variable) # Changes the second prompt list value to the self.variable value
            confirm = input(''.join(prompt)) # Asks user for input with the string of prompt
            return confirm # Returns the confirm variable value

    # Defines get_name function
    def get_name(self):
        prompts = [ # Creates the two promts
            'Choose a name for the instalation: ', # Initial question
            ['Are you sure you want to name it ', '', '? (y/n) '] # Confirmation question
        ]
        return self.get_user_input(*prompts) # Returns the value returned by get_user_input()

    # Defines get_gameDir function
    def get_gameDir(self): # Creates the two promts
        prompts = ['Choose a directory: ', # Initial question
            ['Are you sure you want to use ', '', ' as path? (y/n) '] # Confirmation question
        ]
        while True: # Infinite Loop
            variable = self.get_user_input(*prompts) # Gets the value returned by get_user_input()

            if exists(variable): # Checks if the path exists
                return variable # Returns the variable

            else:
                print('\nDirectory doesnt exists\n') # Prints an error message

    # Defines get_MaxRamArg function
    def get_MaxRamArg(self): # Creates the two promts
        prompts = ['Choose an amount of ram: ', # Initial question
            ['Are you sure you want to use ', '', 'Gb of ram? (y/n) '] # Confirmation question
        ]
        return self.get_user_input(*prompts, True) # Returns the value returned by get_user_input()

    # Defines get_versionId function
    def get_versionId(self):
        if self.mc_loader == 0: # Checks if the mc_loader is 0
            versionId = self.version_to_install # Creates the value for versionId to match the file of the version isntalled

        if self.mc_loader == 1: # Checks if the mc_loader is 0
            versionId = f'{self.version_to_install.split('-')[0]}-forge-{self.version_to_install.split('-')[1]}' # Creates the value for versionId to match the file of the version isntalled

        if self.mc_loader == 2: # Checks if the mc_loader is 0
            versionId = f"fabric-loader-{fabric.get_latest_loader_version()}-{self.version_to_install}" # Creates the value for versionId to match the file of the version isntalled

        if self.mc_loader == 3: # Checks if the mc_loader is 0
            versionId = f"quilt-loader-{quilt.get_latest_loader_version()}-{self.version_to_install}" # Creates the value for versionId to match the file of the version isntalled

        return versionId # Returns versionId value
