# Brand Name Generator
print("Welcome to the Brand Name Generator.")

# assigning variable
city = ""
pet = ""

# check the input city from the user
while True:
    print("What's the name of the city you grew up in?")
    city = input("> ")
    if city == "":
        print("you haven't entered anything. Please try again.")
    else:
        break

# check the input pet from the user
while True:
    print("What's your pet's name?")
    pet = input("> ")
    if pet == "":
        print("you haven't entered anything. Please try again.")
    else:
        break

# output of the brand name
print(f"Your Brand name is {city} {pet}.")
