numbers = open('numbers.txt', 'r')
first_number = int(numbers.readline())
second_number = int(numbers.readline())
final_number = first_number + second_number
print(final_number)