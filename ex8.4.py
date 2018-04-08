
fname = raw_input("Enter file name: ")

fh = open(fname)
words = []

for line in fh:
	words = words + line.split()
	words.sort()

words2=[]

for word in words:

	if word not in words2:
		words2.append(word)

print(words2)