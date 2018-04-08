# file handle as a sequence

xfile = open('text.txt')
for cheese in xfile:
    print(cheese)

# counting lines in a file
fhand = open('text.txt')
count = 0
for line in fhand:
    count = count +1
print('Line Count:', + count)
print('Line Count:', count)

# reading the whole file
fhand = open('file.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])

#Searching through a file
fhand = open('mbox-short.txt')
for lind in fhand:
    if line.startswith('from') :
        print(line)

#Searching through a file (fixed)
#We can strip the whitespace from the right-hand side of the string using rstrip() from the string library.  The newline is considered whitepace and is stripped.

fhand = open('mbox-short.txt')
for lin in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

#Skipping with continue

fhand = open('mbox-short.txt')
for lind in fhand:
    line=line.rstrip()
    if not line.startswith('From') :
        continue
    print(line)
