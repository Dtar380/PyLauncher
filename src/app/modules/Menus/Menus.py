########################################
#####  Import Modules/Libs         #####
########################################

##### External Libs                #####
import minecraft_launcher_lib as MLL

##### Built-in Libs                #####
from os.path import exists, dirname
from sys import path

##### Internal Modules             #####
from modules.System.SystemFunctions import SystemFunctions
from modules.Users.UserManager import UserManager
from modules.Installations.InstallationManager import InstallationManager
from modules.Menus.MenuManager import MenuManager
from modules.Menus.ParametersMenu import InstallationParameters

##### Constants                    #####
from modules.constants import launcher_path

########################################
#####  MenusManager                #####
########################################

#####  Menus class                 #####
class Menus:
    
    def __init__(self, menus, instfile, usfile):
        self.instfile = instfile # Gets the installations file path
        self.usfile = usfile # Gets the users file path
        self.menu_list = {}
        for i in menus: # Iterates in a dictionary qith menus and actions
            # Creates a dictionarie of menus attached to a MenuManager object with their actions
            self.menu_list[f'{i}_menu'] = MenuManager(menus[i])
            
    # Main Menu
    def mainMenu(self):
        # Runs the main_menu object print_menu method and gets the returned index
        index = self.menu_list['main_menu'].print_menu('PyLauncher v0.1.1\nSelect an option:\n')
        menu_actions = [ # Creates a list with the actions to perform acording to index
            self.usersMenu, # Calls userMenu function
            self.executeMenu, # Calls the executeMenu function
            self.createMenu, # Calls createMenu function
            self.installationMenu, # Calls installationMenu function
            exit # Exits the programm
        ]
        menu_actions[index]() # Calls the action in the specified index

    # Users Menu, to operate users
    def usersMenu(self):
        # Runs the users_menu object print_menu method and gets the returned index
        index = self.menu_list['users_menu'].print_menu('Select an option:\n')
        menu_actions = [ # Creates a list with the actions to perform acording to index
            UserManager(self.usfile).select_user, # Calls the select_user method from the UserManager class
            UserManager(self.usfile).delete_user # Calls the delete_user method from the UserManager class
        ]
        if index == 0: # If the index is 0
            UserManager(self.usfile).create_user() # Calls the create_user method from the UserManager class
        else:
            # Creates a list of actions with all the users
            actions = [user.username for user in UserManager(self.usfile).users]

            # Creates a temporal menu with the actions
            userSelection_menu = MenuManager(actions)

            # Runs the temporal menu object print_menu method and gets the returned index
            user = userSelection_menu.print_menu('Select a user:\n')
            menu_actions[index - 1](user) # Calls the action in the specified index

    # Create Menu, to create installations
    def createMenu(self):
        # Checks if the user has internet connection
        if SystemFunctions().get_internetConnection():

            # Runs the users_menu object print_menu method and gets the returned index
            index = self.menu_list['create_menu'].print_menu('Select an MC Loader:\n')
            menu_actions = [ # Creates a list with the actions to perform according to index
                lambda: MLL.utils.get_version_list(), # Gets the minecraft versions
                lambda: MLL.forge.list_forge_versions(), # Gets the forge versions
                lambda: MLL.fabric.get_stable_minecraft_versions(), # Gets the fabric versions
                lambda: MLL.quilt.get_stable_minecraft_versions(), # Gets the quilt versions
                lambda: MLL.utils.get_installed_versions(launcher_path), # Gets the versions all ready installed
                lambda: self.getMrpack(),
            ]
            function = menu_actions[index] # Sets the function choosen in the function
            forks = function() # Set forks with the return of the function choosen

        else:
            # Index will be the same as for the option 4 when having an internet connection
            index = 4
            # Forks must be already installed versions because of lack of internet connection
            forks = MLL.utils.get_installed_versions(launcher_path)

        if index == 5: # If the index is 5 (mrpack)
            version_to_install = forks[1] # Gets the version to install with the .mrpack file

        else: # If index is not 5 (mrpacks)
            version_to_install = self.select_versionId(index, forks) # Gets the version to install

        # Check if the index is lower than 4
        if index < 4:

            # After that checks if the version needs to be installed 
            # Dont use 'if and' with the two clauses in order to be more efficient
            if self.install_version(index, version_to_install):

                # Creates a list with all the installation methods acording to each loader
                install_method = [
                    MLL.install.install_minecraft_version, # Installs vanilla minecraft version
                    MLL.forge.install_forge_version, # Installs forge minecraft version
                    MLL.fabric.install_fabric, # Installs fabric minecraft version
                    MLL.quilt.install_quilt # Installs quit minecraft version
                ]
                # Installs the version with the required method
                install_method[index](version_to_install, launcher_path)

        # Gets the parameters of the using an object from the class InstallationParameterMenu
        parameters = InstallationParameters(True, index, version_to_install)

        if index == 5: # Checks if the index is not 5 (mrpacks)
            SystemFunctions().clear() # Clears the consol

            # Installs the mrpack version on the launcher pack and if there was a selected gameDir
            # Installs the mods and configs on the specified dierectory
            MLL.mrpack.install_mrpack(forks[0], launcher_path, parameters.parameters[1])

        # Uses the create_installation method form InstallationManager passing the parameters as arguments
        InstallationManager(self.instfile).create_installation(*parameters.parameters)

    # Selects a versionId
    def select_versionId(self, MC_LOADER, forks):
        last_forge_version = 0 # Sets first_forge_version to 0
        version_exists = False # Sets version_exists to False

        while not version_exists: # Loop while version doesnt exist
            SystemFunctions().clear() # Clear the consol

            for fork in forks: # Iterates through all forks

                # If the loader is vanilla or custom and is a release
                if (MC_LOADER == 0 or MC_LOADER == 4) and fork['type'] == 'release':
                        print(fork['id']) # Prints the releases versions

                elif MC_LOADER == 1: # If the modloader is forge

                    # Splits the forge version string to two parts
                    forge_version = fork.split('-')[0]

                    # Checks if the forge version was already printed and if its a release
                    if forge_version != last_forge_version and 'pre' not in fork:

                            print(fork) # Prints the latest release forge version

                            # Sets the last forge version as the actual forge verison
                            last_forge_version = forge_version

                elif 1 < MC_LOADER > 4: # If the modloader is fabric or quilt
                    print(fork) # Prints the version

            version_to_install = input('\nSelect a version: ') # Asks for an input

            for fork in forks: # Iterates through all the forks

                # Checks if the loader is vanilla or custom and if the fork matches the input
                if (MC_LOADER == 0 or MC_LOADER == 4) and fork['id'] == version_to_install:
                    version_exists = True # Versions exist
                    break # Break for the loop

                # Checks if the fork matches the input
                elif fork == version_to_install:
                    version_exists = True # Versions exist
                    break # Break for the loop

        return version_to_install # Returns the input

    # Install version, checks if the version is already installed (automated)
    def install_version(self,MC_LOADER,version_to_install):

        # creates a versionId object with the class InstallationParameterMenu using the method get_versionId
        versionId = InstallationParameters(
            mc_loader = MC_LOADER, version_to_install = version_to_install
            ).get_versionId()

        # Returns False if the version already exists and True if its not already installed
        return not any(i['id'] == versionId for i in MLL.utils.get_installed_versions(launcher_path))

    # InstallModPack, for installing .mrpack files
    def getMrpack(self):
        while True: # Infinite loop
            SystemFunctions().clear() # Clears the consol

            # Asks the user to input the path to the .mrpack file
            file_path = input('Enter the path to the .mrpack file:\n')

            if exists(file_path) and '.mrpack' in file_path: # If the file exists and if its a .mrpack file
                # Gets the minecraft loader and version of the modpack
                version_to_install = MLL.mrpack.get_mrpack_launch_version(file_path)
                return [file_path, version_to_install] # Returns the file path
            
            else:
                print('\nFile was not found or is not an .mrpack file\n') # Gives an error

    # Execute Menu, for executing installations
    def executeMenu(self):

        # Calls the selectInstalationMenu function
        installation = self.selectInstalationMenu()

        # Calls the executeInstallation functions passing installation as the argument
        self.executeInstallation(installation)

    # Installation Menu, for managing installations
    def installationMenu(self):
        
        # Calls the selectInstalationMenu function
        installation = self.selectInstalationMenu()
        options = [ # Creates a list with the actions to perform acording to index
            self.executeInstallation, # Executes an installation
            self.openInstallationPath, # Opens the path of an installation
            self.changeParameter, # Used to change the parameters of an installation
            InstallationManager(self.instfile).delete_installation # Used to delete the selected installation
        ]
        # Runs the instalations_menu object print_menu method and gets the returned index
        index = self.menu_list['installation_menu'].print_menu('Select an option:\n')
        options[index](installation) # Runs the option acording to the index

    # Select Installation Menu, for selecting installations
    def selectInstalationMenu(self):
        
        # Creates a list of actions with all the installations
        actions = [inst.name for inst in InstallationManager(self.instfile).installations]
        
        if not actions: # If the menu is empty
            SystemFunctions().clear() # Clear the consol
            print('There are no installations') # Print Error
            return # Return Nothing
        
        # Creates a temporal menu with the actions
        selectInstalation_menu = MenuManager(actions)

        # Returns the index value returned by the print_menu method of the temporal menu object
        return selectInstalation_menu.print_menu('Select a installation:\n')

    # ExecuteInstallation, executes the installation
    def executeInstallation(self, installation):
        # Gets the selected user using the method get_selected_user of the class UserManager
        selected_user = UserManager(self.usfile).get_selected_user()
        # Executes the installation using the methof execute_installation of the class InstallationManager
        InstallationManager(self.instfile).execute_installation(installation, *selected_user)

    # OpenInstallationPath, opens the path on the file explorer
    def openInstallationPath(self, installation):
        # Opens the installation path using the method open_installation_path of the Class InstallationManager
        InstallationManager(self.instfile).open_installation_path(installation)

    # ChangeParameter, menu to change the parameter
    def changeParameter(self, installation):
        # Gets the parameters creating an object of the class InstallationParametersMenu
        parameters = InstallationParameters(forced=False)
        # Changes the parameters of the installation using the method change_parameters of the class InstallationManager
        InstallationManager(self.instfile).change_parameters(installation, *parameters.parameters)
