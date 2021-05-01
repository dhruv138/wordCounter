import re
import sys
import os
import pathlib
import datetime
import warnings
import matplotlib.pyplot as plt
import wordCounter as WC

def multifile_reading_word_counter():

    filepath = ''
    
    #validating presense of file to read
    try:
        filepath = sys.argv[1]
    except IndexError:
        print ("missing file(s) to read")
        print ("run as python wordCounter.py '<filepath>'")
        print ("Example:\npython wordcounter.py 'foo*bar/bar*.txt'")
        return
	
    #validating input by making sure reverse traversal and root traversal is not happening
    if (not filepath or ("../" in filepath) or (filepath.startswith('/')) or ("/~/" in filepath)):
        print ('invalid file path')
        return

    #validating that the passed in file exists
    os.system('ls '+filepath+' >> __reading_files.txt')
    test = open('__reading_files.txt', 'r')
    test2 = test.readline()
    if len(test2)==0:
        print('invalid file path')
        return
    test.close()
    os.system('rm -rf __reading_files.txt')

    #extracting files on which to word count
    found_files = os.popen('ls '+filepath)
    files_to_be_read = found_files.readlines()

    #running the actual word count on the files given
    for file_to_be_read in files_to_be_read:
        file = file_to_be_read[:-1]
        print ('\n###################reading '+file+"###################")
        obj = WC.wordCounter(file)
        obj.print_dictionary_alphabetically()
        obj.letter_counter()
#        list[file].print_letter_count()
        
multifile_reading_word_counter()