"""Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, 
and print out the converted temperature"""

cel=0
celx= input("What is the temperature (in Celcius)?")
try:
    cel=int(celx)
    f= cel * 9/5+32
    print("The temperature is",f,"degrees Fahrenheit")
except:
    print(celx," is not a number.") 
    
