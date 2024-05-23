def euclidean_algorithm(a, b):
    """
    Implementation of the Euclidean Algorithm to find the greatest common divisor (GCD) of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def get_input(prompt):
    """
    Function to get input from the user, ensuring it is a positive integer.
    """
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                raise ValueError("Please enter a positive integer.")
            return num
        except ValueError as e:
            print(e)

def main():
    """
    Main function to execute the Euclidean Algorithm using user input.
    """
    print("Welcome to the Euclidean Algorithm program.")
    print("This program finds the greatest common divisor (GCD) of two numbers.")

    # Get input from the user for the two numbers
    num1 = get_input("Enter the first positive integer: ")
    num2 = get_input("Enter the second positive integer: ")

    # Calculate the greatest common divisor (GCD)
    gcd = euclidean_algorithm(num1, num2)

    # Output the result
    print(f"The greatest common divisor (GCD) of {num1} and {num2} is: {gcd}")

if __name__ == "__main__":
    main()