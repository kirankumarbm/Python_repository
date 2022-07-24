# 1  program for Hello World
print("Hello World")

# 2   program to Add Two Numbers
class Test:
    def __init__(self):
        self.a = input("Enter First Number ")
        self.b = input("Enter Second Number ")

    def add_two(self):
        return float(self.a)+float(self.b)
t = Test()
print("Sum of", t.a, "and", t.b, "is =", t.add_two() )


# 3   program to subtract two numbers
class Test:
    def __init__(self):
        self.a = input("Enter First Number ")
        self.b = input("Enter Second Number ")

    def sub_two(self):
        return float(self.a)-float(self.b)
t = Test()
print("Subtraction of", t.a, "and", t.b, "is =", t.sub_two() )

# 4 Program to Multiply Two numbers
class Test:
    def __init__(self):
        self.a = input("Enter First Number ")
        self.b = input("Enter Second Number ")

    def Mul_two(self):
        return float(self.a) * float(self.b)
t = Test()
print("Multiplication of", t.a, "and", t.b, "is =", t.Mul_two() )

# 5 program for Arithmetic Operations
class Test:
    def __init__(self):
        self.a = input("Enter First Number ")
        self.b = input("Enter Second Number ")

t = Test()
print("Sum of", t.a, "and", t.b, "is =", float(t.a) + float(t.b))
print("Subtraction of", t.a, "and", t.b, "is =", float(t.a) - float(t.b))
print("Multiplication of", t.a, "and", t.b, "is =", float(t.a) * float(t.b))
print("Division of", t.a, "and", t.b, "is =", float(t.a) / float(t.b))
print("Modulus of", t.a, "and", t.b, "is =", float(t.a) % float(t.b))
print("Exponent of", t.a, "and", t.b, "is =", float(t.a) ** float(t.b))


# 6 program to print Calendar
import calendar
year = int(input("Enter the Year : "))
month = int(input("Enter the Month Number, which you want to Display: "))
print(calendar.month(year, month))


# 7 Program to Make a Simple Calculator
import sys
class Calculator:
    @staticmethod
    def add():
        n = int(input("How Many Numbers you want to add "))
        addition = 0
        st = []
        for i in range(n):
            a = int(input("Enter Number "))
            st.append(a)
        for i in st:
            addition = addition + i
        print("Addition of ", end=" ")
        for i in st:
            print(i, end=",")
        print("is =", addition)

    @staticmethod
    def sub():
       a = int(input("Enter First Number "))
       b = int(input("Enter Second Number "))
       print("Subtraction of ", a, " & ", b, " is = ", a-b)

    @staticmethod
    def mul():
        n = int(input("How Many Numbers you want to Multiply "))
        product = 1
        st = []
        for i in range(n):
            a = int(input("Enter Number "))
            st.append(a)
        for i in st:
            product = product * i
        print("Multiplication of ", end=" ")
        for i in st:
            print(i, end=",")
        print("is =", product)

    @staticmethod
    def div():
        a = int(input("Enter First Number "))
        b = int(input("Enter Second Number "))
        print("Division of ", a, " by ", b, " is = ", a/b)

    @staticmethod
    def modulus():
        a = int(input("Enter First Number "))
        b = int(input("Enter Second Number "))
        print("Modulus of ", a, " by ", b, " is = ", a % b)

    @staticmethod
    def exponent():
        a = int(input("Enter First Number "))
        b = int(input("Enter Second Number "))
        print("Exponent of ", a, " by ", b, " is = ", a ** b)

while True:
    print("\n....Enter below code...... \na - Addition\t\ts - Subtraction\nm - Multiplication"
          "\t\td - Division\nmo - Modulus\t\tex - Exponent\ne - Exit")
    option = input("Choose Your Option: ")
    if option.lower() == 'a':
        Calculator.add()
    elif option.lower() == 's':
        Calculator.sub()
    elif option.lower() == 'm':
        Calculator.mul()
    elif option.lower() == 'd':
        Calculator.div()
    elif option.lower() == 'mo':
        Calculator.modulus()
    elif option.lower() == 'ex':
        Calculator.exponent()
    elif option.lower() == "e":
        sys.exit()
    else:
        print("invalid Entry ...... Enter valid Option")

# 8  program to find Cube of a Number
number = float(input("Enter any number to find Cube : "))
cube = number ** 3
print("Cube of a Number is = ", cube)


# 9 program to find the Largest of 2 Numbers
a = float(input(" Please Enter the First Number: "))
b = float(input(" Please Enter the Second Number: "))

if a> b: print(a, "is larger than ", b)
elif b>a: print(b, "is larger than ", a)
elif a == b: print(a," is == to ", b)

# 10  program to find the Largest of 3 Numbers
a = float(input("Please Enter the First Number: "))
b = float(input("Please Enter the Second Number: "))
c = float(input("Please Enter the Third Number: "))

if a>b and a>c: print(a, "is Grater Than Both", b, "&", c)
elif b>a and b>c: print(b, "is Grater Than Both", a, "&", c)
elif c>a and c>b: print(c, "is Grater Than Both", a, "&", b)
elif a == b == c: print("All Three numbers are equal",a)


# 11 program to Print Natural number 1 to N
N = int(input("Enter First N Natural Numbers (N=?) : "))
for i in range(1, N+1):
    print(i, end=" ")


# 12 Python program for Leap Year
year = int(input("Please Enter the Year to check Leap year: "))
if ((year % 400 == 0 ) or
   ((year % 4 ==0) and (year % 100 != 0))):
    print(year, " is a Leap Year")
else: print(year, " is not Leap Year")

# 13 Python program to find Odd or Even
number = int(input(" Please Enter any Integer Value : "))
if number % 2 == 0: print(number," is an Even Number ")
else: print(number, " is an Odd Number ")

# 14 Python program to Print Even Numbers from 1 to 100
for i in range(1, 101):
    if i % 2 == 0: print(i, end=" ")

# 15 Python program to Print Odd Numbers from 1 to 100
for i in range(1, 101):
    if i % 2 != 0: print(i, end=" ")

# 16 Program to Print Negative Numbers in a Range
start = int(input("Enter the Minimum Number = "))
end = int(input("Enter the Maximum Number = "))

print("All Negative Numbers from ", start, " to", end)
for i in range(start, end+1):
    if i < 0: print(i, end=" ")


# 17 Program to Print Positive Numbers in a Range
start = int(input("Enter the Minimum Number = "))
end = int(input("Enter the Maximum Number = "))

print("All Positive Numbers from ", start, " to", end)
for i in range(start, end+1):
    if i > 0: print(i, end=" ")


# 18 Python program to find Positive or Negative
Number = int(input("Enter the  Number = "))

if Number >0: print(Number, " is a Positive Number")
elif Number <0 : print(Number, " is a Negative Number")
else: print("Entered Number is ", Number)

# 19 Python program to find Profit Or Loss
cp = float(input("Enter Cost Price(CP) : "))
sp = float(input("Enter Selling Price(SP) : "))
if sp > cp :
    amt = sp - cp
    print(amt, " Profit occurred ")
elif cp > sp :
    amt = cp - sp
    print(amt, "Loss occurred")
else: print("No Profit, No Loss")


# 20  program to find the Square of a Number
number = float(input(" Please Enter Number : "))
square = number ** 2
print(number, "quare is =", square)

# 21 program to find the Square root of a Number
import math
number = float(input(" Please Enter Number : "))
squareRoot = math.sqrt(number)
print(number, "Square root is=",squareRoot)

# 22 Python Program to find all divisors of an integer
num = int(input(" Enter any integer to find divisors = "))
print("The Divisors of the Number are = ")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")


# 23 Python Program to find Compound Interest

import math
princ_amount = float(input(" Please Enter the Principal Amount : "))
rate_of_int = float(input(" Please Enter the Rate Of Interest   : "))
time_period = float(input(" Please Enter Time period in Years   : "))

ci_future = princ_amount * (math.pow((1 + rate_of_int / 100), time_period))
compound_int = ci_future - princ_amount

print("Future Compound Interest for Principal Amount {0} = {1}".format(princ_amount, ci_future))
print("Compound Interest for Principal Amount {0} = {1}".format(princ_amount, compound_int))


# 24 Python program to check Number Divisible by 5 and 11
n = int(input("Enter number : "))
if n % 5 == 0 and n % 11 == 0:
    print(n, "is divisible by both 5 & 11")
else: print(n, "is not divisible by both 5 & 11 ")


# 25 program to find the Power of a Number
n = float(input("Enter Number : "))
ex = float(input("Enter exponent : "))
print(n," Power", ex, "is =", n ** ex)


# 26 Python program for Multiplication Table
n = int(input("Enter number, for which you want Multiplication Table : "))
for i in range(1, 11):
    print(n, " * ", i, " = ", n*i)


# 27 Python example to find Roots of a Quadratic Equation
import math

a = int(input("Please Enter a Value of a Quadratic Equation : "))
b = int(input("Please Enter b Value of a Quadratic Equation : "))
c = int(input("Please Enter c Value of a Quadratic Equation : "))

discriminant = (b * b) - (4 * a * c)

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant) / (2 * a))
    root2 = (-b - math.sqrt(discriminant) / (2 * a))
    print("Two Distinct Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
elif discriminant == 0:
    root1 = root2 = -b / (2 * a)
    print("Two Equal and Real Roots Exists: root1 = %.2f and root2 = %.2f" %(root1, root2))
elif discriminant < 0:
    root1 = root2 = -b / (2 * a)
    imaginary = math.sqrt(-discriminant) / (2 * a)
    print("Two Distinct Complex Roots Exists: root1 = %.2f+%.2f and root2 = %.2f-%.2f" %(root1, imaginary, root2, imaginary))

# 28  Python example to find Student Grade
english = float(input(" Enter English Marks: "))
math = float(input(" Enter Math score: "))
computers = float(input(" Enter Computer Marks: "))
physics = float(input(" Enter Physics Marks: "))
chemistry = float(input(" Enter Chemistry Marks: "))

total = english + math + computers + physics + chemistry
percentage = (total / 500) * 100

print("Total Marks =",total)
print("Marks Percentage ",percentage)


# 29  Python example to find Simple Interest
P = float(input(" Please Enter the Principal Amount : "))
R = float(input(" Please Enter the Rate Of Interest   : "))
T = float(input(" Please Enter Time period in Years   : "))

SI = (P * R * T) / 100
print("Simple Interest is =",SI)



# 30 Program to Read 10 Numbers and Find their Sum and Average
Sum = 0
print("Please Enter 10 Numbers\n")
for i in range(1, 11):
    num = int(input("Enter number : "))
    Sum = Sum + num

avg = Sum / 10
print("The Sum of 10 Numbers     = ", Sum)
print("The Average of 10 Numbers = ", avg)


# 31 Program to Print First 10 Even Natural Numbers
print(" The First 10 Even Natural Numbers ")
for i in range(1, 11):
    print(2 * i, end=",")

# 32 Program to Print First 10 Natural Numbers
print(" The First 10 Natural Numbers ")
for i in range(1, 11):
    print(i, end=' ')

# 33 Program to Print First 10 Natural Numbers in Reverse
print(" The First 10 Natural Numbers in Reverse")
for i in range(10, 0, -1):
    print(i, end=" ")

# 34 Program to Print First 10 Odd Natural Numbers
print("The First 10 Odd Natural Numbers ")
for i in range(1, 11):
    print(2 * i - 1, end=" ")

# 35 program to Print Natural number 1 to N
number = int(input("Please Enter Number (N- value): "))
for i in range(1, number + 1):
    print (i, end=' ')


# 36 program to Print Natural Numbers in Reverse Order
number = int(input("Please Enter Number (N- value): "))
for i in range(number, 0, -1):
    print (i, end=' ')

# 37 Program to Find the Sum and Average Of Three Numbers
num1 = float(input("Please Enter the First Number  = "))
num2 = float(input("Please Enter the Second number = "))
num3 = float(input("Please Enter the Third number  = "))

sum = num1 + num2 + num3
avg = sum / 3
print("Sum of ",num1,num2, "and",num3, "= ", sum)
print("Average of ",num1,num2, "and",num3, "= ", avg)


# 38 Program to Find the Average Of Two Numbers
x = int(input("Please Enter the First Number  = "))
y = int(input("Please Enter the Second number = "))
sum = x + y
avgOfTwo = sum / 2
print("Average of", x, "&", y, "is ", avgOfTwo)

# 39 Python example to find Sum and Average of Natural Numbers
number = int(input("Enter Number: "))
total = 0
for value in range(1, number + 1):
    total = total + value
average = total / number
print("Sum of", number, " natural numbers is", total)
print("Average of", number, " natural numbers is", average)


# 40 Python Program to Find Sum of 10 Numbers and Skip Negative Numbers
Sum = 0
print("Please Enter 10 Numbers to Find Positive Sum")
for i in range(1, 11):
    num = int(input("Enter Number : "))
    if num < 0:
        continue
    Sum = Sum + num
print("The Sum of 10 Numbers by Skipping Negative Numbers = ", Sum)

# 41 Python Program to Find Sum of 10 Numbers until a user enters Positive Numbers
Sum = 0
print("Please Enter 10 Numbers to Find Positive Sum")
for i in range(1, 11):
    num = int(input("Enter Number : "))
    if num < 0:
        break
    Sum = Sum + num
print("The Sum of Positive Numbers = ", Sum)


# 42 Python example to Calculate Electricity Bill
units = int(input(" Please enter Number of Units you Consumed : "))
if units < 50:
    amount = units * 2.60
    surcharge = 25
elif units <= 100:
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35
elif units <= 200:
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45
else:
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75
total = amount + surcharge
print("Electricity Bill = ", total)

# 43  Program to Find Distance Between Two Points
import math
x1 = int(input("Enter the First Point Coordinate x1  = "))
y1 = int(input("Enter the First Point Coordinate y1  = "))
x2 = int(input("Enter the Second Point Coordinate x2 = "))
y2 = int(input("Enter the Second Point Coordinate y2 = "))
x = math.pow((x2 - x1), 2)
y = math.pow((y2 - y1), 2)
print(x)
print(y)
print(math.sqrt(x + y))
distance = math.sqrt(x + y)
print('The Distance Between Two Points is ', distance)


# 44 Python program to find Total Average & Percentage of 5 Subjects
english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))
total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total / 500) * 100
print("Total Marks = ", total)
print("Average Marks = ", average)
print("Marks Percentage = ", percentage)


# 45 Python Program to Get Current Date and Time
from datetime import datetime
now = datetime.now()
print("Current Date and Time =", now)












































































