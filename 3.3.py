"""Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error message.  
If the score is between 0.0 and 1.0, print a grade using the following table:
score grade
>=.9    a
>=.8    b
>=.7    c
>=.6    d
<.6     f
"""
inp= input("enter score")

try:
    score= float(inp)
    if score >=0 and score <=1.0:
        if score >= 0.9:
            print('A')
        elif score >= 0.8:
            print('B')
        elif score >= 0.7:
            print('C')
        elif score >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print("bad score")
except:
    print("Please type a score")