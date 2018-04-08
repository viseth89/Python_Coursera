#Opening the file using a 'with' establishes a context that automatically closes the file avoiding problems in the future

with open('romeo.txt') as file:
	lines = file.readlines()

words = []
for line in lines:
	split_line = line.split()
	words.extend(split_line)

#For some reason, doing it in this manner seems to automatically sort the files, still trying to understand why

words.sort()
print(words)