# Automatic Door Agent.
while True:
    person = input("Is a person detected? (yes/no):").strip().lower()
    if person == "yes":
        print("Door Open")
        break
    elif person == "no":
        print("Door Closed")
        break
    else:
        print("Invalid input! Please enter only yes or no.")
