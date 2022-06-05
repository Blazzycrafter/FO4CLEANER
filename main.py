# file version 0.1 fo4
import subprocess
import os

try:
    from settings import *
    if fileversion != "0.2":
        int('r')
except:
    print("settings.py not found or file version wrong. creating...")
    with open("settings.py", "w") as f:
        f.write("""
#DO NOT EDIT THIS ENTRY
#This file is automatically generated by the cleaner.
#if this entry is edited, the cleaner will rewirite the entiere settings.py file
# updated from 0.1 to 0.2
fileversion = "0.2"


#path to Game root directory
#default: C:\Program Files (x86)\Steam\steamapps\common\Fallout 4
# hint do not use "\\" in the path ... use \\\\ instead
path = "E:\\\\SteamLibrary\\\\steamapps\\\\common\\\\Fallout 4"

#data directory
#default: C:\Program Files (x86)\Steam\steamapps\common\Fallout 4\Data
# or short: path + "\\\\Data"
# use \\\\ instead of "\\"
data = path + "\\Data"


# in this files are the files that need to be copied / cleaned stored as a list
# example for sse:
# master_list = "master_list.txt" > ["Skyrim.esm", "Update.esm", "HearthFires.esm", "Dragonborn.esm", "Dawnguard.esm"]
# clean_list = "clean_list.txt" > [ "Update.esm", "HearthFires.esm", "Dragonborn.esm", "Dawnguard.esm"]
master_list = "masterlist.txt"
clean_list = "clean_masterlist.txt"


# path to F04Edit
# use \\\\ instead of "\\"
# path + executable file name (c:\\.....\\F04Edit.exe)
xedit = "C:\\\\Program Files (x86)\\\\FO4Edit\\\\FO4Edit.exe"

# game
# please set your game here or it will be tryed to use the name of xedit....
# here are the inforemation from official documentation... (i hope its right...)
# •  -<gamemode> can be any of the following: ['tes5vr', 'fo4vr', 'tes4', 'tes5', 'enderal', 'sse', 'fo3', 'fnv', 'fo4', 'fo76']
# example
# game="-fo3"
game = ""

""")
    print("settings.py created. please edit it and run the script again.")
    exit()
CopyFileList = []
CleanFileList = []



def loadTxt():
    global CleanFileList
    with open(clean_list, "r") as file:
        for line in file:
            CleanFileList.append(line.strip())


def SSEEDIT():
    global data, xedit, game
    for ESMFile in CleanFileList:
        print("cleaning "+ESMFile+"...")
        if game != "":
            args = f'{xedit} -quickautoclean -autoexit -autoload "{ESMFile}" -D:"{data}" {game}'
        else:
            args = f'{xedit} -quickautoclean -autoexit -autoload "{ESMFile}" -D:"{data}"'
        print(args)
        subprocess.call(args, shell=False)

            


def cleanNames(CleanFileList):
    x = []
    for ESMFile in CleanFileList:
        if ESMFile.find(" ") != -1:
          x.append(f'\"{ESMFile}\"')
        else:
          x.append(ESMFile)
    return x


if __name__ == '__main__':
    loadTxt()
    print(CleanFileList)
    print(path)

    CleanFileList = cleanNames(CleanFileList)
    print(CleanFileList)

    SSEEDIT()
