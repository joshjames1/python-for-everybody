"""write a program to open the file romeo.txt and read it line by line.  For each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list.  If the word is not in the list, add it to the list.  When the program completes, sort and print 
the resulting words in alphabetical order."""

#open romeo file
#for loop on each line and split
#check if word exists in list, if not, add it. 
#sort list
#print list
list1=[] #create empty list
fhand= open('romeo.txt')
for line in fhand:
    listsplit= line.split()
    for i in listsplit:
        if i not in list1:
            list1.append(i)
list1.sort()
print(list1)