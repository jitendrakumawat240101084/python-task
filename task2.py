print("=== Personalized Greeting Program ===")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

full_name = first_name.strip().title() + " " + last_name.strip().title()

print("\nHello,", full_name + "! Welcome to the Python program.")
