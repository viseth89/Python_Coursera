# Use words.txt as the file name
fname = raw_input("Enter file name: ")
fh = open(fname)

for file in fh:
    ly = file.rstrip()
    print(ly.upper())

