"""add a easter egg on previous example"""
count=0
total=0
fhand=input("Enter file name: ")
try:
    if fhand=="hey hey":
        print("you like hey, hey too?")
    else: 
        fhandle= open(fhand)
for line in fhandle:
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