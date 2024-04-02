# Tip Calculator

print("Welcome to the Tip Calculator")

base_bill = ""
tip = ""
people = ""

# get the base bill amount without tip
while True:
    print("Enter the bill amount?")
    base_bill = input("> $")
    if float(base_bill) < 0:
        print("Bill amount can't be negative. Please try again.")
    else:
        break

# get the percentage of the tip
while True:
    print("What percentage tip would you like to give? 10, 12, or 15?")
    percentage = input("> ")
    choice_list = ['10','12','15']
    if percentage not in choice_list:
        print("Please enter 10 or 12 or 15")
    else:
        break

# get the number of people to split the bill
while True:
    print("Enter the total number of people to split the bill?")
    people = input("> ")
    if people == 0:
        print("Please enter the number of people 1,2,3?")
    else:
        break

# add the tip to the base bill
total_bill = float(base_bill) * (1 + int(percentage) / 100)

# calculate the split bill and round the bill to 2 decimal places.
split_bill = round(total_bill / int(people),2)

print(f"Each people bill amount is {split_bill}")
