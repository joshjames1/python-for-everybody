"""Write a program to prompt the user for hours and rate per hour to copmuter gross pay"""
hours= input("How many hours?")
rate=input("What is the pay rate?")

hoursx= float(hours)
ratex= float(rate)

gross_pay= hoursx * ratex
print (gross_pay)