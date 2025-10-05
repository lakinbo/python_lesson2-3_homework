# Create a program that converts human years to pet years for different animals.

# Requirements:

# Ask for pet type (dog, cat, bird, hamster)
# Ask for pet's age in human years
# Convert using these formulas:
    # Dog: First 2 years = 24 pet years, then 4 years for each additional year
    # Cat: First 2 years = 24 pet years, then 4 years for each additional year
    # Bird: Multiply by 9
    # Hamster: Multiply by 25
# Display the converted age with a fun message

pet_type = ""
human_years = 0
pet_years = 0

try:
    while (pet_type != "dog" or pet_type != "cat" or pet_type != "bird" or pet_type != "hamster"):
        pet_type = input("Enter pet type (dog/cat/bird/hamster): ")#.lower()

    while human_years <1 or human_years> 20:
        human_years = int(input("Enter your pet's age in human years: "))

    if pet_type == "dog":
        pet_years = (min(2, human_years) * 12) + (max(0, human_years - 2) * 4)
    elif pet_type == "cat":
        pet_years = (min(2, human_years) * 24) + (max(0, human_years - 2) * 4)
    elif pet_type == "bird":
        pet_years = human_years * 9
    elif pet_type == "hamster":
        pet_years = human_years * 25

    print("=== PET AGE CONVERSION ===")
    print(f"Pet Type: {pet_type.title()}")
    print(f"Human Age: {human_years} years")
    print(f"Pet Age: {pet_years} pet years")
    print()
    print(f"Fun Fact: Your {pet_type.lower()} is like a {pet_years}-year-old human!")

except Exception as e:
    print("Invalid input!!!")


