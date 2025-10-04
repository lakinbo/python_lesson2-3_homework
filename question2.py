# Create a program that takes a restaurant order and calculates the bill based on menu choices.

# Requirements:

# Display a menu with 4 food options and prices:
    # 1. Pizza - $15.99
    # 2. Burger - $12.50
    # 3. Salad - $9.99
    # 4. Pasta - $13.75
# Ask user to choose by number (1-4)
# Ask if they want a drink (+$2.50)
# Calculate total with 8% tax
# Display itemized bill

choice = 0
food_option = ""
food_price = 0
drink_choice = None
drink_price = 0
tax_rate = 0.08

try:
    while choice <1 or choice > 4:
        choice = int(input("Enter your choice (1 - 4): \n"))

    if choice == 1:
        food_option = "Pizza"
        food_price = 15.90
    elif choice == 2:
        food_option = "Burger"
        food_price = 12.50
    elif choice == 3:
        food_option = "Salad"
        food_price = 9.90
    elif choice == 4:
        food_option = "Pasta"
        food_price = 13.75



    # while drink_choice != "yes" or drink_choice != "no":
    drink_choice = input("Would you like a drink? (+$2.50) (yes/no): \n").lower()

    if drink_choice == "yes":
        drink_price = 2.50

    tax = tax_rate * (food_price + drink_price)

    print("======= ITEMISED BILL =======")
    print(f"Menu option selected: {food_option}")
    print(f"Food      :    {food_price:.2f}")
    print(f"Drink     :    {drink_price:.2f}")
    print("--------------------")
    print(f"Sub-Total :    {(food_price + drink_price):.2f}")
    print(f"Tax       :    {tax:.2f}")
    print("--------------------")
    print(f"Total     :    {(food_price + drink_price + tax):.2f}")
    print("====================")
    print("Thank you for your purchase!")

except Exception as e:
    print("Invalid input!!!")
