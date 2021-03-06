 #! /usr/bin/env python

# export PATH="~/Documents/collections/code/toc:$PATH"



# IMPORTS
import os



# SETTINGS
# feel free to adapt as needed

standard_toc_file = "toc.md"
verbose_mode = True
current_working_directory = os.getcwd()



# debug settings
debug_mode = False



##### FUNCTIONS #####
def vprint(message): # verbose printing
    if verbose_mode: print(message)



def dprint(message): # debug printing
    if debug_mode:
        print("********** TOC: " + message)



def readTocFile(file_path):
    dprint('recognizing file paths...')

    toc_file = list(open(file_path))
    all_files_in_toc = []

    # find file references in TOC file (lines starting with "/")
    for line in toc_file:
        if line[0] == '/':
            all_files_in_toc.append(line.replace('\n',''))

    # print all_files_in_toc
    if len(all_files_in_toc) > 0:
        for path in all_files_in_toc:
            vprint(path)
    else:
        print("Your TOC file exists but is empty.")

    dprint('recognized file paths.')



##### CLASSES #####
class File:
    def __init__(self, path, name):
        dprint('initializing File...')
        self.path = path
        self.name = name
        self.file_path = path + "/" + name
        dprint('initialized File.')



##### READ TOC FILES #####
os.listdir(current_working_directory)

toc_file_path = current_working_directory + "/" + standard_toc_file
try:
    readTocFile(toc_file_path) # read paths in file
except FileNotFoundError:
    choice = input("There is no TOC file here. Would you like to create one? (Y/n)").lower()
    if choice == "y" or " ":
        os.system('"${EDITOR:-vi}" toc.md') # open an empty file if there is none yet

dprint(toc_file_path)



##### QUIT PROGRAM #####

dprint('quit.')
