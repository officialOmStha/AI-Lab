# Goal-Based Vacuum Cleaner Agent

room_A = input("Enter the state of the room A '(Dirty/Clean)'.\n").strip().lower()
room_B = input("Enter the state of the room B '(Dirty/Clean)'.\n").strip().lower()
room = input("Enter the current room '(A/B)': \n")

if room == 'A':
    if room_A == 'dirty':
        print("Clean Room A")
        room_A = 'clean'
        room = 'B'

elif room == 'B':
    if room_B == 'dirty':
        print("Clean Room A")
        room_B = 'clean'
        room = 'A'

if room_A == 'clean' and room_B == 'clean':
    print("Goal Acheived")

