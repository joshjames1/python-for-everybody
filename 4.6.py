"""Rewrite your pay computation with time and a half for overtime and create a function called computepay which takes two 
parameters (hours and rate)"""


def computepay(hours,rate):
    if hours > 40.0:
        OThours= hours -40
        OTPay= OThours * rate *1.5
        RegularPay= 40 * rate
        GrossPay= OTPay + RegularPay
        print("Total amount paid:", GrossPay)
    else:
        GrossPay= hours * rate
        print("Total amount paid:",GrossPay)
    
inphours= input("How many hours worked?")
try:
    hours= float(inphours)
except:
    print("Not a number")
    quit()
inprate=input("What is the pay rate?")
try:
    rate= float(inprate)
except:
    print("Not a rate")
    quit()
    
computepay(hours,rate)
