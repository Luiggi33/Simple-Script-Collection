# -*- coding: utf-8 -*-
"""
@author: luiggi33
"""

#importing os to get the files
import os
#importing shutil to move files
import shutil

# Select the Path you want to Sort it to
outputpath = 'Path/To/Sort/It/To'
# Select the Path from where to Sort
inputpath = 'From/Where/To/Sort'

# List all Things in the input dir
list_ = os.listdir(inputpath)

# go thru every file in the list
for file_ in list_:
    
#   splicing to extract the type of the file
    name, ext = os.path.splitext(file_)

    ext = ext[1:]

#   Skipping if invalid
    if ext == '':
        continue
    
#   Skipping if the file to sort is a directory
    if os.path.isdir(outputpath + '/' + file_):
        list_.remove(file_)
        print( file_ + " didnt get moved because its a directory.")
        continue
        
#   if a folder already exists, move it
    if os.path.exists(outputpath+'/'+ext):
        shutil.move(outputpath+'/'+file_, outputpath+'/'+ext+'/'+file_)
        print(name + " got moved to " + outputpath+'/'+ext+'/'+file_)

#   if a folder doesnt exists, create it and then move it
    else:
        os.makedirs(outputpath+'/'+ext)
        shutil.move(outputpath+'/'+file_, outputpath+'/'+ext+'/'+file_)
        print(name + " got moved to " + outputpath+'/'+ext+'/'+file_)