# Write a Python program that calculates movie ticket costs with different pricing.

# Requirements:

# Ask the user for their name and age
# Set ticket prices: 
    # Child (under 13): $8
    # Adult(13−64):$12
    # Senior (65+): $9
# Ask how many tickets they want (Ticket prices should be calculated based on the age of the person buying them)
# Calculate total cost and display a receipt-style output
# Use f-string formatting for the receipt

ticket_price = 0
age = 0
quantity = 0

name = input("Name: ")

try:
    while age <= 1 or age >= 120:
        age = int(input("Age: "))

        if age > 0 and age < 13:
            ticket_type = "Child"
            ticket_price = 8
        elif age >=13 and age <= 64:
            ticket_type = "Adult"
            ticket_price = 12
        elif age >= 65 and age <= 120:
            ticket_type = "Senior"
            ticket_price = 9

    while quantity <=1 or quantity >= 200:
        quantity = int(input("How many tickets do you want?"))

    print("=== MOVIE TICKET RECEIPT ===")
    print(f"Customer: {name}")
    print(f"Ticket Type: {ticket_type} (${ticket_price:.2f} each)")
    print(f"Quantity: {quantity}")
    print(f"Total Cost: ${ticket_price * quantity:.2f}")
    print("Thank you for your purchase!")

except Exception as e:
    print("Invalid input!!!")

