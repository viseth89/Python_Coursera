# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
score = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count += 1
    score += float(line[20:])

average = score/count
print('Average spam confidence: ' + str(average))

