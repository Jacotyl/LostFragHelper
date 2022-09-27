#Lost Frag Helper ver.0.1 
#Jacob Tyler, 9/26/22

import os
import sys 
import binascii

versionNumber = 0.1

def buildFileList(path): #Returns a list of every single file's path within a given folder.
    for root, dirs, files in os.walk(cwd+path):
        for name in files:
            if name.endswith("_XOR"):
                print(f"File {name} has already been previously modified. Skiping.")
            else:
                #print(f"Adding {os.path.join(root, name)} to mod list!")
                fileList.append(os.path.join(root, name))


def checkFolderExists(folder): #Check if specified folder in cwd exists. Returns 1 if true, 0 if false.
    folderPath = cwd + folder
    if (os.path.exists(folderPath)):
        return 1
    else:
        return 0

def fileXOR(file):
    filename = os.path.basename(file)
    b = bytearray(open(file,"rb").read()) #Read file, XOR the first 0x400 bytes with 0xFF, then write to file.pack_XOR
    for i in range(0, 0x400): 
        b[i] ^= 0xFF
    try:
        open(file+"_XOR", "xb").write(b)
    except FileExistsError as e:
        print("Error: File already exists, skipping. ")
   


if __name__ == "__main__":

    print(f"LostFragHelper ver.{versionNumber} running from: {os.getcwd()}")
    
    cwd = os.getcwd()

    folders = [
        #"/Master",
        #"/Synonym",
        #"/Text",
        #"/UnitParts",
        "/Background",
        "/CharacterTex",
        "/Effect",
        "/Equipment",
        "/Exploration",
        "/Foreground",
        "/Gacha",
        "/Item",
        "/Koikoi",
        "/Materials",
        "/Panel",
        "/PatternFade",
        "/Quest",
        "/Raid",
        "/Sound",
        "/Stage",
        "/Still"
        
    ]

    fileList = []
    
    for item in folders:
        if checkFolderExists(item) != 1:
            print(f"folder {item} not found! Removing from list of files to modify!")
            folders.remove(item)
    if not folders:
        print("No supported files found. Are you sure that LostFragHelper.py is in the correct folder?")

    for items in folders:
        buildFileList(items)
    
    for item in fileList:
        fileXOR(item)

    print("File modification complete. Files with the .pack_XOR extension should now be compatible with AssetStudio.")
