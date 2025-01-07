# Define a function to print a greeting message
def greet(name):
    """This function takes a name and prints a greeting message."""
    print(f"Hello, {name}!")

# Define a function to calculate the square of a number
def square(number):
    """This function takes a number and returns its square."""
    return number ** 2

# Main section of the program
if __name__ == "__main__":
    # Call greet function
    greet("Alice")
    
    # Call square function and store the result
    result = square(5)
    
    # Print the result of the square function
    print(f"The square of 5 is: {result}")
