import os, send2trash

def deleteFile(folder):
    folderPath = os.path.abspath(folder)     # Specify folder to be deleted
    for foldername, subfolders, filenames in os.walk(folderPath):
        for filename in filenames:
            filePath = folderPath + '/' + filename     # Individual file paths for each file inside folder
            if os.path.getsize(filePath) > 200:
                x = os.path.getsize(filePath)
                print(filename, x)
                send2trash.send2trash(filePath)     # All removed files are sent to recycle bind 

deleteFile('randomQuizGenratorResults')

