with open('romeo.txt') as file:
	lines = file.readlines()

words = []
for line in lines:
	split_line = line.split()
	words.extend(split_line)

words.sort()
print(words)