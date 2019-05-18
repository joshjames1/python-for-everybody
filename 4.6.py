"""Rewrite your pay computation with time and a half for overtime and create a function called computepay which takes two 
parameters (horus and rate)"""

hours= input("How many hours worked?")
rate=input("What is the pay rate?")
try:
    hoursx= float(hours)
    ratex= float(rate)
    if hoursx > 40:
        OThours= hoursx -40
        OTPay= OThours * Ratex *1.5
        RegularPay= 40 * ratex
        GrossPay= OTPay + RegularPay
        Print("Total amount paid:", GrossPay)
    else:
        GrossPay= hoursx * ratex
        print("Total amount paid:",GrossPay)
except:
    print("Please enter numbers")