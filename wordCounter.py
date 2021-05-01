import re
import sys
import os
import pathlib
import datetime
import warnings
import matplotlib.pyplot as plt

class wordCounter:

    def __init__(self, filename):
        self.WCdictionary = {}
        self.sorted_list = []
        self.unique_letter_count = {}
        self.filename = ''
        
        self.filename=filename
        ####
        #### run program as "python wordCounter.py '<file to be counted>'"
        ####
        #preprocessing
        time_program_init = datetime.datetime.now()
        words = self.extract_data()
        time_data_extract = datetime.datetime.now()
        time_to_data_extraction = time_data_extract - time_program_init
        
        #counting
        time_word_count_start = datetime.datetime.now()
        self.word_count(words)
        time_word_count_end = datetime.datetime.now()
        time_to_word_count = time_word_count_end - time_word_count_start

        #post processing
        time_postprocess_start = datetime.datetime.now()
        self.sort_dictionary()
        #self.print_dictionary_alphabetically()

        #time processing
        time_program_end = datetime.datetime.now()
        time_to_post_process = time_program_end - time_postprocess_start
        total_execution_time = time_program_end - time_program_init
        #self.plot_dictionary_alphabetically()
        
        print("time to preprocess data: "+str(time_to_data_extraction)[6:11]+" in seconds")
        print("time to count words: "+str(time_to_word_count)[6:11]+" in seconds")
        print("time to post process: "+str(time_to_post_process)[6:11]+" in seconds")
        print("total time to execute: "+str(total_execution_time)[6:11]+" in seconds")

      #	print_dictionary()
      #	plot_dictionary()

    #function responsible for reducing the string to a readable format and removing punctuation
    def preprocess(self, OriginalString):
        str = OriginalString
        lower_str=str.lower()
        no_punc = re.sub(r'[^\w\s]', '', lower_str)
        splitted = no_punc.split()
        
        return splitted

    #function responsible for compliling a list of all of the words in the text        
    def extract_data(self):
        words =[]
        with  open(self.filename, 'r') as file:
            for str in file.readlines():
                processed = self.preprocess(str)
                words.extend(processed)
        file.close()
        
        return words

    #Hashmapping function responsible for accounting for word frequency
    def word_count(self, words):
        for word in words:
            try:
                self.WCdictionary[word] += 1
            except KeyError:
                self.WCdictionary[word] = 1

    def letter_counter(self):
        for word in self.WCdictionary:
            for letter in word:
                try:
                    self.unique_letter_count[letter] += self.WCdictionary[word]
                except KeyError:
                    self.unique_letter_count[letter] = self.WCdictionary[word]

    #iterate through frequncy list to print output
    def print_dictionary(self):
        for tuple in self.WCdictionary:
            print (tuple+" : "+str(self.WCdictionary[tuple]))

    #iterate through frequncy list to print output using sorted list as key
    def print_dictionary_alphabetically(self):
        for key in self.sorted_list:
            print (key+" : "+str(self.WCdictionary[key]))

    def print_letter_count(self):
        for tuple in self.unique_letter_count:
            print (tuple+" : "+str(self.unique_letter_count[tuple]))

    #plotting fucntion to show graphical representation of frequency map
    def plot_dictionary(self):
        warnings.filterwarnings("ignore")
        key = []
        value = []

        for tuple in self.WCdictionary:
            key.append(tuple)
            value.append(self.WCdictionary[tuple])
        
        fig = plt.figure(1)
        ax = fig.add_subplot(111)
        plt.bar(key, value)
        ax.set_xticklabels(key, fontsize = 6, rotation = 90)
        plt.show()
   
    #plotting fucntion to show graphical representation of frequency map, keyed alphabetically
    def plot_dictionary_alphabetically(self):
        warnings.filterwarnings("ignore")
        value = []

        for key in self.sorted_list:
            value.append(self.WCdictionary[key])
        
        fig = plt.figure(1)
        ax = fig.add_subplot(111)
        plt.bar(self.sorted_list, value)
        ax.set_xticklabels(self.sorted_list, fontsize = 6, rotation = 90)
        plt.xlabel('unique word')
        plt.ylabel('rate of occurrence')
        plt.title("Word frequency")
        plt.show()

    #sorting function to create aplhabetically sorted list of keys
    def sort_dictionary(self):
        self.sorted_list = sorted(self.WCdictionary.keys(), key=str.lower)
