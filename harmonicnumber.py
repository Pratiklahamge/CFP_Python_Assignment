'''
@Author : pratik lahamge
@Date : 17-2-2022
@python: 3.7
@Title : Harmonic Number
a. Desc -> Prints the Nth harmonic number: 1/1 + 1/2 + ... + 1/N.
b. I/P -> The Harmonic Value N. Ensure N != 0
c. Logic -> compute 1/1 + 1/2 + 1/3 + ... + 1/N
d. O/P -> Print the Nth Harmonic Value.
'''


def Harmonic(n):
    sum = 0
    for i in range(1, n + 1):
     sum = sum + 1 / i
    print(sum)


n = int(input("Enter the number:"))
Harmonic(n)
