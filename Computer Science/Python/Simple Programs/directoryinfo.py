import os

#print the current directory
print(os.getcwd())

#list out directory(sub-directories)
#print(os.listdir())

#create directory -- comment out after 1 run
#os.mkdir('test')

#change directory -- comment out after 1 run
#move up one level to parent
#os.chdir("..")

#print(os.getcwd())

#os.walk will produce directory tree
# for root, dirs, files in os.walk('.'):
#     print(f"Root: {root}")
#     print(f"Directories: {dirs}")
#     print(f"Files: {files}\n")
    
#remove directories
#os.rmdir('test')
    
#remove non-empty directories
#requires shutil
    
#shutil.rmtree("thedirectory")
    
#get size file
print("File size: ", os.path.getsize('/Users/sahivlopez/Documents/Python Code 2024/tax.py'), "bytes")

#get last mod time
print("Last modified: ", os.path.getmtime('/Users/sahivlopez/Documents/Python Code 2024/tax.py'))

