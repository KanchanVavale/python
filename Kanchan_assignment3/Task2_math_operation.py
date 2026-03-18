#calculation using math module.
import math

try:
    num = int(input("Enter any number: "))
    if num <= 0:
        print("Please enter positive number")
    else:
        #Square root of the number
        squareroot = math.sqrt(num)
        print("Square root: ", squareroot)

        #Natural logarithm (log base e) of the number
        log_of_num = math.log(num)
        print("Logarithm: ", log_of_num)

        #Sine of the number (in radians)
        sin_of_num = math.sin(num)
        print("Sine: ", sin_of_num)


except ValueError:
    print("Invalid Input! Please enter only positive number")

