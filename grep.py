#Grep Program - Vince Ye
#Goal: grep str filename should return all lines that contain 'str'

import sys


def findlines (strsearch, filename):
	inputfile = open(filename, 'r')	
	linenum = 0	
	
	for line in inputfile:
		linenum += 1
		if strsearch in line:
			print(str(linenum) + ": " + line)
		

		
		

#search_file = input("Enter File to Search: ")
#search_string = input("Enter String to Search For: ")
findlines(sys.argv[1], sys.argv[2])

#print(findlines(str(search_file), str(search_string)))
#print(search_file)
