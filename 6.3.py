"""Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments."""

def count(word, letter):
    count = 0
    for something in word:
        if something == letter:    # must use ==, = will not work
            count = count + 1
    print(count)

word = 'banana'
letter= 'n'
count(word, letter)

