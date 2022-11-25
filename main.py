import math


# Program make a simple scientific calculator

# This function adds two numbers
def add(a, b):
    return a + b


# This function subtracts two numbers
def subtract(a, b):
    return a - b


# This function multiplies two numbers
def multiply(a, b):
    return a * b


# This function divides two numbers
def divide(a, b):
    if b!=0:
        return a / b
    else:
        return "Undefined"


# This function finds remainder
def mod(a, b):
    return a % b


# This function finds sine value
def sine(x):
    return math.sin(x)


# This function finds cosine value
def cosine(x):
    return math.cos(x)


# This function finds tangent value
def tangent(x):
    return math.tan(x)


# This function finds sq_root
def sq_root(x):
    return x ** (1 / 2)


# This function finds power
def power(a, b):
    return a ** b


# This function finds degree
def deg(x):
    return math.degrees(x)


# This function finds radian
def rad(x):
    return math.radians(x)


print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.mod(%)")
print("6.Sine")
print("7.Cosine")
print("8.Tangent")
print("9.Square root")
print("10.Exponent(power(a^b))")
print("11.Radian to Degree")
print("12.Degree to Radian")

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10/11/12): ")

    # check if choice is one of the six options
    if choice in ('1', '2', '3', '4', '5', '10'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "%", num2, "=", mod(num1, num2))


        elif choice == '10':
            print(num1, "**", num2, "=", power(num1, num2))

        elif choice == '11':
            print("Radian of " + str(x), "=", rad(x))

        elif choice == '12':
            print("Degree of " + str(x), "=", deg(x))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    elif choice in ('6', '7', '8', '9', '11', '12'):
        x = float(input('Enter a number: '))
        if choice == '6':
            print("Sine(" + str(x) + ") =", sine(x))

        elif choice == '7':
            print("Cosine(" + str(x) + ") =", cosine(x))

        elif choice == '8':
            print("tangent(" + str(x) + ") =", tangent(x))

        elif choice == '9':
            print("Square root of " + str(x), "=", sq_root(x))

        elif choice == '11':
            print("Radian of " + str(x), "=", rad(x))

        elif choice == '12':
            print("Degree of " + str(x), "=", deg(x))

        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
