#! /usr/bin/env python3
# Timmy Williams
# CS 4375 Fall 2018
# Python Intro

import sys # for parameter passing at command line
import re  # Use of re to split strings
import os  # To access files
from collections import Counter # Use of iterable hash table


# Determine correct paramater are passed at call
if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output file>")
    exit()
    

inputTextFile = sys.argv[1]
outputTextFile = sys.argv[2]


# File to be read from to build the Key,Value pair hash table
f = open(inputTextFile)


# Grab all lines of text from file
wordcountTemp = f.read()


# Remove everything except characters and spaces
wordcountTemp2 = re.split('\W+' , wordcountTemp)


# Create Key,Value paired hash table
wordcount = Counter(wordcountTemp2)


# Check if declared file to be created already exists,
#if so, remove file and recreate. Otherwise just
#create file.
if os.path.exists(outputTextFile):
    os.remove(outputTextFile)
    

#Creating outpute file.
mySpeechKey = open(outputTextFile, "w+")


# Write to created output file the Key,Value pair hash table
# in either Ascending or Descending order. Our test script
# provided by Instructor compared key alphabetically, so reverse
# is set to false, however descending order can be achieved
# simply by flipping to true.
for key, value in sorted(wordcount.items(),reverse = False):
    mySpeechKey.write(key+' '+str(value)+'\n')
