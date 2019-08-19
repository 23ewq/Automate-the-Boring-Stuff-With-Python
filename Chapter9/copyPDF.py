import shutil, os

def backupToPDF(folder):
    folder = os.path.abspath(folder)   # Gets absolute path of the folder to be copied
    if not os.path.exists('newFolder'):
        os.makedirs('newFolder')         # If the new folder to be made doesn't exist, make it
    for foldername, subfolders, filenames in os.walk(folder):
        print(foldername)            
        for filename in filenames:
            if filename.endswith('.pdf'):      # All the files ending with .pdf will be copied to new folder
                x = os.path.basename(filename)
                print(filename)
                shutil.copy(folder + '/' + x, os.path.abspath('newFolder') + '/' + x )

backupToPDF('example')
        
