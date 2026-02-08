# Goal based destination reach

current = input("Enter the current location: \n").strip().lower()
destination = input("Enter the destination location: \n").strip().lower()

if current != destination:
    print("Move Towards the destination.")
elif current == destination:
    print("Destination Reached.")
