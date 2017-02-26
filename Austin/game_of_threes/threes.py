#!/usr/bin/python
#A game of threes implementation by Austin Smitherman
def threes(num):
    while num != 1:
        print(num)
        if num % 3 == 0:
            num = num/3
        elif (num - 1) % 3 == 0:
            num -= 1
            num = num/3
        elif (num + 1) % 3 == 0:
            num += 1
            num = num/3


threes(31337357)
# threes(5)
# threes(4)
