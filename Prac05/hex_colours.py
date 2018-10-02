HEX_COLOURS = {"azure": "#f0ffff", "beige": "#f5f5dc", "cyan": "#00ffff", "gray": "#bebebe", "gold": "#ffd700", "light":
                "#eedd82", "orchid": "#da70d6", "pink": "#ffc0cb", "purple": "#a020f0", "red": "#ff000"}

def main():
    user_code = input("Please input a oolour: ")
    if user_code in HEX_COLOURS:
        print(HEX_COLOURS[user_code])

    else:
        print("This is not in the data base")

main()