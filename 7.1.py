"""Write a program to read through a file and print the contents of the file (line by line) all in upper case.
Executing the program will look at follows:

mbox-short.txt"""

#open file handle
fhand= open('mbox-short.txt')
for line in fhand:
    line= line.rstrip().upper()
    print(line)



#print contents one line at a time