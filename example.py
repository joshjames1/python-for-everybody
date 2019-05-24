fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

count = 0
fh = open(fname)
for line in fh:
	print(line)