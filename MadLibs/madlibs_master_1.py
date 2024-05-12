import os
import webbrowser
from madlibs_data_1 import * #Import story IDs, titles, and word banks

# Ask user which MadLib they want to do
valid_ID = False
while valid_ID!=True:
    story_ID = input('Which story do you want to do? ')

    # Check if user inputted a number. If not ask them to redo input.
    if story_ID.isdigit() == False:
        print("Error. Must input number between 1-" + madlibs_count)

    # Check if the input is valid for the number of stories available
    # If input is valid, move on. Otherwise ask user to redo input.
    elif int(story_ID) > 0 and int(story_ID) < int(madlibs_count)+1:
        valid_ID = True
        print("\nLoading "+title[int(story_ID)-1]+' ...\n')
    else:
        print("Error. Must input number between 1-" + madlibs_count)

# File paths and variables
fpath = os.path.dirname(os.path.realpath(__file__))
fname_blank = "madlib_" + story_ID + "_BLANK.html"
fname_filled = "madlib_" + story_ID + "_FILLED.html"
fpath_blank = os.path.join(fpath+"/blank_madlibs",fname_blank)
fpath_filled = os.path.join(fpath+"/filled_madlibs",fname_filled)

# Ask user for missing words and put input into word bank array
for i in range(len(wordBank[int(story_ID)-1])):
    wordBank[int(story_ID)-1][i][2] = input(wordBank[int(story_ID)-1][i][0]+': ')

# Insert words into text
# First, open blank text and save data into variable
f = open(fpath_blank,'r',encoding='utf8')
filedata = f.read()
f.close()

# Replace wordBank words
for i in range(len(wordBank[int(story_ID)-1])):
    filedata = filedata.replace("<i><b>"+wordBank[int(story_ID)-1][i][1],"<i><b>"+wordBank[int(story_ID)-1][i][2])

# Determine name for new html file.
# Check if file already exists. If not, save file. If it does, ask the user for a new file name. Repeat until the user gives a file name that doesn't exist.
if os.path.exists(fpath_filled):
    overwrite_status = input("File already exists. Overwrite? (y/n) ")
    if overwrite_status == 'y' or overwrite_status == 'Y' or overwrite_status == 'yes' or overwrite_status == 'Yes':
        print("Overwriting previous save file...")
    else:
        fileExists = True
        while fileExists:
            fname = input("File already exists. Input new file name (do not include file type extension): ")
            fpath_filled = os.path.join(fpath+"/filled_madlibs",fname+'.html')
            if os.path.exists(fpath_filled) == False:
                fileExists = False

# Save text to the new file.    
f=open(fpath_filled,'w')
f.write(filedata)
f.close()

# Open filled text in browser
#chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
#webbrowser.get(chrome_path).open(fpath_filled, new=2)  # open in new tab
webbrowser.open(fpath_filled, new=2)  # open in new tab