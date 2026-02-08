# Fire Alarm System

smoke = input("Enter '(Fire)' if there is fire. \n").strip().lower()

if smoke == 'fire':
    print("Turn Alarm ON.")
else:
    print("Turn Alarm OFF.")