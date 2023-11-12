# program that accepts an integer (n) and computes the value of n+nn+nnn.
# Sample value of n is 4
# Expected Result : 492
enter=str(input("Enter the Number"))
n=0
for i in range(1,4):
    l=enter*i
    print(l)
    l=n+int(l)
    n=l
print("Total of the above:",n)


# program to create a histogram from a given list of integers.
symb=input("Enter the symbol")
seq=input("Enter the sequence")
list=seq.split(',')
int_list=[int(i) for i in list]
for m in int_list:
    print(symb*m)


# Python function that takes two lists and returns True if they have at least one common member
z=[1,2,3,4]
x=[4,5,6,7]
def check(z,x):
    for i in z:
        if i in x:
            print(True)
check(z,x)


# program to print the numbers of a specified list after removing even numbers from it.
z=[5,7,2,3,4]
for i in z:
    if i%2==0:
        z.remove(i)
print(z)




#  program to print the following string in a specific format (see the output).
# Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are"
# Output :
    
print("Twinke Twinkle Little Star\n     How i wonder what you are\n         Up above the world so high\n            Like a diamond in the sky")

#  program to find out what version of Python you are using.
import sys
print(sys.version)
print(sys.version_info)
print(sys.api_version)


# program to display the current date and time.
import time
print(time.asctime())

# program that calculates the area of a circle based on the radius entered by the user.
import math
radius=float(input("Enter the radius"))
area=(math.pi)*(radius**2)
print("Area of Circle is",area)


# program that accepts the user's first and last name and prints them in reverse order with a space between them.
firstname=input("Enter your first name")
secondname=input("Enter your second name")
print(secondname,'',firstname)

# program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
Numbers=input("Enter the numbers")
lis=Numbers.split(',')
tup=tuple(lis)
print('list',lis)
print('tuple',tup)

# program that accepts a filename from the user and prints the extension of the file.
filename=input("Enter the file name")
z=list(filename.split('.'))

print(z[1])
if z[1]=='py':
    print("it is a python file")
elif z[1]=='java':print("It is a java file")
elif z[1]=='txt':print("It is a txt file")
else:print("This may be some other type of file")

# program to display the first and last colors from the following list.
colors=input("Enter the list of colors seperating with commas")
z=colors.split(',')
print(z[0],z[-1])

# program that prints the calendar for a given month and year.
import calendar
year=int(input("Please enter the year"))
month=int(input("Please enter the month"))
z=calendar.month(year,month)
print(z)

# program to get the volume of a sphere with radius six.
import math
radius=float(input("Enter the radius of sphere"))
volume=4/3*((math.pi)*(radius**3))
print("The volume of sphere is:",volume)

# program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
string=input("enter any statement")
z=string.startswith('if')
if z==True:
    print(string)
else:
    print('if',string)

# program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
num=int(input("Enter any number"))
if num%2==0:
    print("Given number is Even\nThank you")
elif num<2:
    print("Entered number is less than two\nPlease try again")
else:
    print("Entered number is odd")

# program to test whether a passed letter is a vowel or not.
letter=input("Enter any one alphabet letter")
vowels=['a','e','i','o','u']
if (letter in vowels)==True:
    print("Entered alphabet is vowel")
else:
    print("Entered alphabet is not vowel")

# program to print all even numbers from a given list of numbers in the same order and stop printing any after 237 in the sequence.
numbers = [    
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 
    958,743, 527
    ]
for i in numbers:
    if i%2==0:
        print(i)
    if i==237:
        break

# program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.

z=[2,3,5,1]
x=[1,2,3,5,7,11]
count=0
for i in z:
    if i==1:
        count=count-1
    for j in range(2,i):
        if i%j==0:
            break
    else:
        count=count+1
if count==len(z):
    print(True)
else:
    print(False)


    

# program that prints out all colors from color_list_1 that are not present in color_list_2.
# Test Data :
# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])
# program that will accept the base and height of a triangle and compute its area.
height=float(input("Please enter the height"))
base=float(input("Please enter the base of the triangle"))
area_of_triangle=(0.5*height*base)
print(area_of_triangle)

# program to calculate the distance between the points (x1, y1) and (x2, y2).
import math
x1=int(input("Enter the x1 value"))
x2=int(input("Enter the x2 value"))
y1=int(input("Enter the y1 value"))
y2=int(input("Enter the y2 value"))
            #pythagorean theorem
dist=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
print("The distance between the two coordinates is:",dist)


# program to check whether a file exists.
import os
os.path.exists('path')

# program to determine if a Python shell is executing in 32bit or 64bit mode on OS.
import platform
platform.architecture()

# program to retrieve the path and name of the file currently being executed.
import os
os.getcwd()
os.path.realpath(__file__)

# program to find out the number of CPUs used.
import multiprocessing
multiprocessing.cpu_count()
            #or
import os
os.cpu_count()

# program to list all files in a directory
import os
os.listdir()

import itertools
s=[[1,2,3],[2,3,4],[13,234,5]]
z=list(itertools.chain(*s))