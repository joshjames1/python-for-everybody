
count = 0
total = 0
while True: 
    inp=input("Enter a number:")
    if inp== "done": break
    else:
        try:
            number= float(inp)
            total= total + number
            count= count +1
            average= total / count
        except:
            print("not a number")
print("count:",count,"total:",total,"average:",average)

