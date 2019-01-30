import os

print("Current DIR ", os.getcwd())  # get current working directory
print("List DIR", os.listdir())  # show all folder and file current directory
# os.makedir('file path') #make a new directory
# os.makedirs('folder/folder/file')
# os.rmdir('file path') #delete diectory
# os.removedirs('filepath/filepath') # delete deep level directory
#os.rename("actual file",'rename file')

print("Main Python file ", os.stat('main.py'))  # print the file meta data
print(os.environ.get('HOME'))
print(os.path.exists('/temp/file.txt'))
print(os.path.splitext('/temp/file.csv'))
print(dir(os.path))
