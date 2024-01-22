########################################
#####  Import/Install libraries    #####
########################################
from os.path import join, exists
from os import mkdir, system, name
from sys import executable
from time import sleep
from json import loads, dump
from subprocess import check_call

libraries = ['minecraft-launcher-lib','install-jdk','uuid'] # List of all libraries to install

for library in libraries: # Iterates on the list to take each library
    check_call([executable, "-m","pip","install",library]) # Installs the library

import minecraft_launcher_lib.runtime as JVM # Importing MLL after installing it
import jdk # Importing the install-jdk after installing it

########################################
#####  Create Directories/Files    #####
########################################

# Paths and files to create
from app.modules.constants import launcher_path, launcher_files_path, files
directories = [launcher_path, launcher_files_path]

# Revise directories/files and create them
for directory in directories: # Iterates through the directories
    if not exists(directory): mkdir(directory) # Creates them if the path doesnt exists

for file in files: # Iterates through the files
    if not exists(join(launcher_files_path, file)): # Checks if the files exist
        with open(join(launcher_files_path, file), 'x') as f: pass # Creates the new file

########################################
#####  Install JVM/JDK             #####
########################################

# Install JVM
runtimes = JVM.get_jvm_runtimes() # Gets the JVM runtimes names

for runtime in runtimes: # Iterates through the JVM runtimes
    if runtime not in [runtimes[3],runtimes[5]]: # Checks is a desired JVM
        JVM.install_jvm_runtime(runtime, launcher_path) # Installes the JVM

# Instal JDK
JDK_path = join(launcher_path,'java') # Path for JDK instalation

while True: # Starts an infinite loop
    system('cls' if name == 'nt' else 'clear') # Clears the terminal
    y_n = input('install Java? (y/n)') # Asks the user if he wants to install Java (y/n)

    if y_n is 'y': # Checks i answer is y
        if not exists(JDK_path): mkdir(JDK_path) # Creates the JDK_path if it doesnt exist
        jdk.install('17',vendor="Adoptium",path=JDK_path) # Installs JDK on JDK_path

    elif y_n is 'n': # Checks i answer is n
        print('Skipping JDK instalation process') # Gives information to user
        break

    else:
        print('Input not valid') # Reports failed request
        sleep(1) # Stops the program fro 1 second
