#Factorial using recursion 
def fact(num):
    """
    Calculate the factorial of a number using recursion.

    Parameters:
    num (int): The number whose factorial needs to be calculated.

    Returns:
    int: Factorial of the number if valid
    None: If the number is negative
    """

    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
        return None
    elif num == 0 or num == 1:
        return 1
    else:
        return num * fact(num - 1)


if __name__ == "__main__":
    
    try:
        num = int(input("Enter a number: "))
        result = fact(num)

        if result is not None:
            print(f"Factorial of {num} is: {result}")

    except ValueError:
        print("Error: Please enter a valid integer.")



