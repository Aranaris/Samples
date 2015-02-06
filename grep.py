#Grep Program - Vince Ye
#Goal: grep str filename should return all lines that contain 'str'


def findlines (filename, strsearch):
		inputfile = open(filename, 'r')
		output = []
		
		
		for line in inputfile:
			if strsearch in line:
				output.append(line)
		
		if len(output) < 1:
			failsearch = "No lines contain that string"
			return failsearch
		
		return output
		
		


search_file = input("Enter File to Search: ")
search_string = input("Enter String to Search For: ")

print(findlines(str(search_file), str(search_string)))
#print(search_file)
