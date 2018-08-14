"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? When a non intger is entered into either numerator or denominator
2. When will a ZeroDivisionError occur? When Zero is entered as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError? Add a If statement to check if it is a zero and if so, say it is invalid.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("That is a invalid input")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")