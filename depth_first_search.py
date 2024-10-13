""" Python implementation of depth-first search algorithm """


from os import listdir
from os.path import isfile, join


def print_filenames(dir):
    """ Recursively prints filenames from given directory """
    for file in sorted(listdir(dir)):
        full_path = join(dir, file)
        if isfile(full_path):
            print(file)
        # below else handles behaviour when certain path is a folder, not a file
        # this is also the clue of depth-first: it'll go inside file structure down to the bottom
        else:
            print_filenames(full_path)

print_filenames(".idea")
