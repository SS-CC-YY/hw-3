# Name: Chenyu Song
# Course: CS 362
# Description: conditions for leap years with error handling
# Due: 04/10/2021


while True:
    try:
        year = int(input("Enter a year: "))# get the input from user
        year = int(year)
    except:
        print("Invaild input!\n")#check the input
    else:
        if(year % 4 == 0 and year % 100 != 0 or year % 400 == 0):#check the leap
            print(year, "is a leap year!")
        else:
            print(year, "is not a leap year!")
        break
