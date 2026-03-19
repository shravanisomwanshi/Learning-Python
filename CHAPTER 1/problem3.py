import os

#specify the directory u want to list
directory_path = '/SHRAVANI'

#list all files annd directories in the specified path
contents = os.listdir(directory_path)

#print each file and directory name
for item in contents:
    print(item)