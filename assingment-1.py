# Q1
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q2
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q3
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# Q4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greatest:", a)
elif b > a:
    print("Greatest:", b)
else:
    print("Both are equal")

# Q5
age = int(input("Enter age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Q6
ch = input("Enter a character: ").lower()
if ch in "aeiou":
    print("Vowel")
elif ch.isalpha():
    print("Consonant")
else:
    print("Not an alphabet")

# Q7
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# Q8
num = int(input("Enter a number: "))
num_str = str(abs(num))
if len(num_str) == 1:
    print("Single-digit number")
elif len(num_str) == 2:
    print("Two-digit number")
else:
    print("More than two digits")

# Q9
marks = int(input("Enter marks: "))
if marks >= 40:
    print("Pass")
else:
    print("Fail")

# Q10
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 7 == 0:
    print("Multiple of both 3 and 7")
else:
    print("Not a multiple of both 3 and 7")
