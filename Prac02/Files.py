username = input("What is your name? ")
OUTPUT_FILE = "username.txt"
out_file = open(OUTPUT_FILE, 'w')
print(username, file=out_file)
