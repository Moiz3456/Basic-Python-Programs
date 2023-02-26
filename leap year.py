#Program to find the the given number is leap year or not
#Program to find the number of leap years in given range
#program to print all the leap years in given range
d=int(input("Please choose any one option regarding leap year programs\n1) To find out the given number is leap year or not\n2) To find out the number of leap years in given range\n3) To print all the leap years in given range\n"))
def leapYear():
    n=int(input("Enter a year"))
    if n%4==0:
        print("Entered year", n ," is a Leap Year\nThank You")
    else:
        print("Entered Year", n ," is not a Leap Year\nPlease Try Again.")


def numOfLeapYears():
    f=int(input("Please Enter the starting range to find all the number of leap years\n"))
    z=int(input("Plese Enter the ending range to find all the number of leap years\n"))
    k=0
    for f in range(f,z):
        if f%4==0:
            k=k+1
    print('The number of leap years in the given range are', k)

def LeapYears():
    f=int(input("Please Enter the starting range to find all the number of leap years\n"))
    z=int(input("Plese Enter the ending range to find all the number of leap years\n"))
    print("Below are the leap years in the given range")
    for f in range(f,z):
        if f%4==0:
            print(f)
    if f<0:
        print("Please enter only positive numbers")
    print("Thank You")
if d==1:
    leapYear()
elif d==2:
    numOfLeapYears()
elif d==3:
    LeapYears()
else:
    print("Sorry, Refresh and Enter only one from the above Options")
    
        
