"""Write another program that prompts for a list of numbers as above and at the end prints out both the max and min of the numbers
instead of the average"""

count = 0
total = 0
max = None
min = None

while True: 
    inp=input("Enter a number:")
    if inp== "done": break
    else:
        try:
            number= float(inp)
            total= total + number
            count= count +1
            if max is None or number> max:    #added "is" instead of "= None"
                max = number
            if min is None or number < min:
                    min= number
        except:
            print("not a number")
print("count:",count,"total:",total,"max:",max, "min", min)