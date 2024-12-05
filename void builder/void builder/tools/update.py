import os
from time import sleep
from zipfile import ZipFile

import requests


class Update():
    def __init__(self):
        self.version = '1.0.0'
        self.github = 'https://raw.githubusercontent.com/Astralopgt/void-builder/refs/heads/main/void%20builder/void%20builder/tools/update.py'
        self.zipfile = 'https://github.com/Astralopgt/void-builder/archive/refs/tags/v1.0.0.zip'
        self.update_checker()

    def update_checker(self):
        code = requests.get(self.github).text
        if "self.version = '1.0.0'" in code:
            print('This version is up to date!')
            print('Exiting...')
            sleep(2)
            exit()
        else:
            print('''
$$\   $$\                               $$\   $$\                 $$\            $$\               
$$$\  $$ |                              $$ |  $$ |                $$ |           $$ |              
$$$$\ $$ | $$$$$$\  $$\  $$\  $$\       $$ |  $$ | $$$$$$\   $$$$$$$ | $$$$$$\ $$$$$$\    $$$$$$\  
$$ $$\$$ |$$  __$$\ $$ | $$ | $$ |      $$ |  $$ |$$  __$$\ $$  __$$ | \____$$\\_$$  _|  $$  __$$\ 
$$ \$$$$ |$$$$$$$$ |$$ | $$ | $$ |      $$ |  $$ |$$ /  $$ |$$ /  $$ | $$$$$$$ | $$ |    $$$$$$$$ |
$$ |\$$$ |$$   ____|$$ | $$ | $$ |      $$ |  $$ |$$ |  $$ |$$ |  $$ |$$  __$$ | $$ |$$\ $$   ____|
$$ | \$$ |\$$$$$$$\ \$$$$$\$$$$  |      \$$$$$$  |$$$$$$$  |\$$$$$$$ |\$$$$$$$ | \$$$$  |\$$$$$$$\ 
\__|  \__| \_______| \_____\____/        \______/ $$  ____/  \_______| \_______|  \____/  \_______|
                                                  $$ |                                             
                                                  $$ |                                             
                                                  \__|            ''')
            choice = input('\nWould you like to update? (y/n): ')
            if choice.lower() == 'y':
                new_version_source = requests.get(self.zipfile)
                with open("void-builder-main.zip", 'wb')as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("void-builder-main.zip", 'r') as filezip:
                    filezip.extractall(path=os.path.join(os.path.expanduser("~"), "Desktop"))
                os.remove("void-builder-main.zip")
                print('The new void builder is dowloaded.\nUpdate Complete!')
                print("OPEN BUILDER.PYW!")
                sleep(5)
            if choice.lower() == 'n':
                print('OPEN BUILDER.PYW!')
                sleep(5)
                exit()


if __name__ == '__main__':
    Update()
