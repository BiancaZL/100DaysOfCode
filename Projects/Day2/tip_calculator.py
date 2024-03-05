print("Welcome to the tip calculator! \n")

bill = float(input("What was the total bill?\n"))
percent = float(input("\nWhat percentage tip would you like to give?\n"))
people = int(input("\nHow many people to split the bill?\n"))

calc = round((bill + (bill * (percent / 100))) / people, 2)

format_calc = "{:.2f}".format(calc)

print(f"\nEach person should pay: ${format_calc}\n")