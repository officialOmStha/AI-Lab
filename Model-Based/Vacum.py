# Model-Based Vacuum Cleaner Agent

room_A = input("Enter status of Room A (dirty/clean): ").lower()
room_B = input("Enter status of Room B (dirty/clean): ").lower()
current_room = input("Current room (A/B): ").upper()

if current_room == "A":
    if room_A == "dirty":
        print("Action: Clean Room A")
        room_A = "clean"
    elif room_B == "dirty":
        print("Action: Move to Room B")
    else:
        print("Action: No operation, all rooms clean")
        
elif current_room == "B":
    if room_B == "dirty":
        print("Action: Clean Room B")
        room_B = "clean"
    elif room_A == "dirty":
        print("Action: Move to Room A")
    else:
        print("Action: No operation, all rooms clean")
