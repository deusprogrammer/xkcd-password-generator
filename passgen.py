#!/usr/bin/python

import random
import sys
import os.path
import argparse

# Parse command line arguments
parser = argparse.ArgumentParser(description='Create a secure password')
parser.add_argument('--dict', dest='dictionaryFile', type=str, 
					default='/usr/share/dict/words' if os.path.isfile('/usr/share/dict/words') else '/usr/dict/words',
					help='What dictionary to use')
parser.add_argument('--words', dest='words', type=int, default=4,
					help='How many words the password should be made up of')
parser.add_argument('--wordSize', dest='wordSize', type=int, default=-1,
					help='How big each word needs to be')
args = parser.parse_args()

# Store parsed arguments
words = args.words
wordSize = args.wordSize
dictionaryFile = args.dictionaryFile

# State variables
password = ""
wordsFound = 0

# Read all lines of dictionary file into memory
with open(dictionaryFile) as f:
	lines = f.read().splitlines()

# Pick random words until we find the requested number of words of the requested size.
while wordsFound < words:
	random.seed()
	n = random.randint(0, len(lines) - 1)
	word = lines[n]
	if wordSize == -1 or len(word) == wordSize:
		password = password + word.lower().title()
		wordsFound = wordsFound + 1

print(password)