'''
@Author : pratik lahamge
@Date : 17-2-2022
@python: 3.722
@Title : Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not
'''

print("Enter a year")
year = int(input())
if (year % 100 == 0) and (year % 400 == 0) or (year % 4 == 0):
    print('This is Leap Year')
else:
    print('This is Not Leap Year')
