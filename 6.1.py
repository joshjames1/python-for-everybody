"""Write a while loop that starts at the last character in the string and works its way backwards to the first character
in the string, printing each letter on a separate line, except backwards."""
index = 0
inp="Word"
index= len(inp)-1
while index >= 0:
    letter= inp[index]
    print(letter)
    index = index -1
