import random

AMOUNT_IN_LINE = 6
MINIMUM = 1
MAXIMUM = 45

def main():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 0:
        print("Error")
        number_of_picks = int(input("How many quick picks? "))

    for i in range(number_of_picks):
        picks = []
        for j in range(AMOUNT_IN_LINE):
            numbers = random.randint(MINIMUM, MAXIMUM)
            while numbers in picks:
                numbers = random.randint(MINIMUM, MAXIMUM)
            picks.append(numbers)
        picks.sort()
        print(" ".join("{:2}".format(numbers) for number in picks))

main()