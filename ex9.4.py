# #Video 9.1-9.2 examples = 

# # counts = dict()
# # names = ['viseth', 'abby', 'tyson', 'penny', 'viseth', 'abby', 'abby', 'tyson', 'penny', 'abby', 'viseth','abby', 'abby', 'tyson']

# # counts2 = dict()

# # for name in names :
# # 	if name not in counts:
# # 		counts[name] = 1
# # 	else:
# # 		counts[name]=counts[name] + 1


# # for name in names :
# # 	counts2[name]=counts2.get(name, 0) + 1

# # print(counts)
# # print('part 2')
# # print(counts2)


# #Video 9.3
# counts = dict()
# print('Enter a line of text:') 
# line = input('Enter some words :') #<--- How come this input isn't treated as a string?

# line = str(line) #<--- This didn't work either, 

# #   File "<string>", line 1
# #    what is going on here                   ^
# #SyntaxError: invalid syntax

# words = line.split()

# print('Words:', words)

# print('Counting...')
# for word in words:
# 	counts[word]=counts.get(word,0) +1
# print('Counts', counts)

# ## Why isn't the input accepted as a string? I have to put quotes, whats the workaround?

# ##Definate loops and dictionaries

# counts = {'chuck' : 1, 'fred' : 42, 'jan':100}
# for key in counts:
# 	print(key, counts[key])



# 8 minute mark example

name = input('Enter file:')
handle = open(name)

counts = dict()
for line in handle:
	words = line.split()
	for word in words:
		counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print(bigword, bigcount)

# exercise example

name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    line.rstrip()
    if line.startswith('From '):
		words = line.split()
		for word in words:
			counts[word] = counts.get(word,0) + 1
			print(words[1])

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print(bigword, bigcount)

#Working answer - will break down and review

name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    line.rstrip()
    if line.startswith('From '):
		line = line.split()
		line = line[1]
		counts[line] = counts.get(line, 0) +1

bigcount = None
bigword = None
for word,count in counts.items():
	if bigcount is None or count > bigcount:
		bigword = word
		bigcount = count

print(bigword, bigcount)





