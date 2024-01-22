########################################
#####  Import Modules/libs         #####
########################################

##### Built-in libs                #####
from subprocess import run
from os import chdir
from os.path import join

##### Internal modules             #####
from modules.Menus.Menus import Menus
from modules.constants import launcher_path, launcher_files_path, files

########################################
#####  Variables                   #####
########################################

# Files
instfile = join(launcher_files_path, files[0])
usfile = join(launcher_files_path, files[1])

# Menus
menus = {
    "main": [
        'Users',
        'Execute Installation',
        'Create Installation',
        'Installation manager',
        'Exit'
    ],
    "users": [
        'Create user',
        'Change user',
        'Delete user'
    ],
    "create": [
        'Vanilla',
        'Forge',
        'Fabric',
        'Quilt'
    ],
    "installation": [
        'Execute Installation',
        'Open game directory',
        'Change parameters',
        'Delete Installation'
    ]
}

########################################
#####  APPLICATION                 #####
########################################

if __name__ == "__main__":
    chdir(launcher_path)
    Menu = Menus(menus, instfile, usfile)
    while True:
        Menu.mainMenu()
