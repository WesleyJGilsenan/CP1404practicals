
def main():
    numbers = []
    for i in range(5):
        number = int(input("number: "))
        numbers.append(number)

    print("First number: ", numbers[0])
    print("Last number: ", numbers[-1])
    print("smallest number: ", min(numbers))
    print("Largest number: ", max(numbers))
    print("Average number: ", sum(numbers)/5)


main()

