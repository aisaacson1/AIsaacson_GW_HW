# The list of pies to print to the screen
pie_list = ["Pecan", "Apple Crisp", "Bean", "Banoffee", "Black Bun", "Blueberry", "Buko", "Burek", "Tamale", "Steak"]

# The list used to store all of the pies selected inside of
pie_cart = []

print("Welcome to the House of Pies! Here are our pies: \n______________________________________________________________ \n")

# Print all of the pies to the screen and their index in brackets
for i in range(len(pie_list)):
    print("(" + str(i) + ") " + pie_list[i], end=", ")


# Set answer to "yes" for while loop
answer = "yes"


while answer == "yes" or answer == "y" or answer == "Yes" or answer == "Y":

    # Ask which pie the user would like to buy
    print("\n \nWhich pie would you like to bring home?")
    selected = input("Input the number of the pie you want: \n")

    # Add the pie at the index chosen to the pie_cart list
    pie_cart.append(pie_list[int(selected)])
    
    print(f"Great! We'll have that {pie_list[int(selected)]} pie right out for you.")
    # ask the user if they want more pies
    answer = input("Would you like to make another selection? ('yes' or 'no') ")


# Loop through the pie_cart to say what pies were brought home
print(f"You purchased {len(pie_cart)} pies:\n")
for pie in pie_list:
    totalpie = pie_cart.count(pie)
    print(f"{totalpie} {pie}")
