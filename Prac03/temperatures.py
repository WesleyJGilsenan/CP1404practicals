def temp_C_To_F (celsius):
    fahrenheit = (celsius *1.8) + 32
    return fahrenheit

def temp_F_To_C (fahrenheit):
    celsius = (fahrenheit - 32) * .5556
    return celsius


def main():
    Answer = input("Would you like to convert Celsius to Fahrenheit or Fahrenheit to Celsius? (C or F)")
    if Answer == ("c"):
        temp_C = int(input("What in celsius would you like to convert to fahrenheit? "))
        temp_F = temp_C_To_F(temp_C)
        print(temp_F, "Degrees Fahrenheit")

    elif Answer == ("f"):
        temp_F = int(input("What in fahrenheit would you like to convert to celsius? "))
        temp_C = temp_F_To_C(temp_F)
        print(temp_C, "Degrees Celsius")

    else:
        print("Error, that is invalid")
        Answer = input("Would you like to convert Celsius to Fahrenheit or Fahrenheit to Celsius? (C or F)")


main()