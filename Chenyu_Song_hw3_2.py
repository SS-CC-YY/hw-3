# Name: Chenyu Song
# Course: CS 362
# Description: conditions for leap years without error handling
# Due: 04/25/2021

year = int(input("Enter a year: "))

if(year % 4 == 0 and year % 100 != 0 or year % 400 ==0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap yar")