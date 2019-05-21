"""Write a program to prompt for a file name, and then read through the file and look for lines of the form:
X-DSPAM-Confidence: 0.8475
When you encounter a line that starts with x-spam -confience: pull apart the line to extract the floating-point number on the
 line.  Count the lines and then compute the total of the spam confidence values from these lines.  When you reach the end of the 
file, print out the average spam confidence. """


#open file handle
count=0
total=0
inp=input("Enter file name: ")
fhand= open(inp)
for line in fhand:
    line=line.strip() 
    if line.startswith("X-DSPAM-Confidence:"):
        start= line.find(" ") +1
        ending= line[start:]
        ending= float(ending)
        total= total + ending
        count= count +1  #count the lines
average= total/count
print(count, average)



#print contents one line at a time