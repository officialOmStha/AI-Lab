# Goal-Based Automatic Door Agent

door = input("Enter the state of the door '(open/closed)'").strip().lower()
outside = input("Enter 'yes' if person is outside, else 'no").strip().lower()

if door == 'closed' and outside == 'yes':
    print("Open The Door.")
elif door == 'open' and outside == 'no':
    print("Close  The Door.")
else:
    print("No Action.")