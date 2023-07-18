# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."



def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."


# Example usage

num1 = int(input("Enter the first Number : "));
num2 = int(input("Enter the second Number : "))

division_result = divide_numbers(num1, num2);
print(division_result)
