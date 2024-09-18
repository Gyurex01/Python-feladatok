"""
Write code to get output below:

What is your first name? First
What is your last name? Last
What is your location? Texas
What is your age? 54
Hi First Last! Your location is Texas and you are 54 years old.
>>>
"""

First = input('First Name:')
Last = input('Last Name:')
Location = input('Your Location:')
Age = int(input("Your age:"))

print('Hi',First,Last,'!' ,'Your location is',Location,'and you are',Age ,'years old.')