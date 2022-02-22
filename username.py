'''
@Author : pratik lahamge
@Date : 17-2-2022
@python: 3.7
@Title : User Input and Replace String Template “Hello <<UserName>>, How are you?”

a. I/P -> Take User Name as Input. Ensure UserName has min 3 char
b. Logic -> Replace <<UserName>> with the proper name
c. O/P -> Print the String with User Name
'''


Username = str(input("Enter Username"))

if len(Username) >= 3:
    print("Hello," + Username + " How Are You ?")
else:
    print(Username, "Not Valid")
    print("Enter Minimum 3 Char Username")
