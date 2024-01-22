from os.path import join
from os import environ as env

# Directories
launcher_path = join(env['APPDATA'], '.mylauncher')
launcher_files_path = join(launcher_path, 'launcher')
files = ['installations.json','users.json']