"""Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter 
and returns a grade as a string.
score grade
>=.9    a
>=.8    b
>=.7    c
>=.6    d
<.6     f
"""

def computegrade(score):
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

inp= input("enter score")
try:
    score= float(inp)
except:
    print("Please type a score")

computegrade(score)