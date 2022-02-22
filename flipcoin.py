'''
@Author : pratik lahamge
@Date : 17-2-2022
@python: 3.7
@Title : Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. Ensure it is positive integer.
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails
'''

import random


def userInput():
    x = int(input("Please Enter number of times you would like to flip coin : \n"))
    if x < 1:
        raise ValueError(" Only nonzero Positive Values can Be passed")
    return x


def flipCoin(n):
    head_count = 0
    tail_count = 0
    for i in range(n):
        x = random.randint(0, 1)
        if x == 1:
            head_count += 1
        elif x == 0:
            tail_count += 1
