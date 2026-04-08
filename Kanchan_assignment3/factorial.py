#Factorial using recursion 
def fact(num):
    """
    FUNCTION TO CALCULATE FACTORIAL OF A NUMBER
    """
    if num < 0:
        print("Please enter positive number.")
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)

try:
    num = int(input("Enter a number: "))
    result = fact(num)

    if result  is not None:
        print(f"Factorial of {num} is: {result}")

except ValueError:
    print("Please enter a number")



