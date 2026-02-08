# Model Based smart light agent.

light_state = 'OFF'
motion = input("Enter '(yes/no)' for motion:\n").strip().lower()

if motion == 'yes' and light_state == 'OFF':
    print("Turn Light ON\n")
    light_state = 'ON'
elif motion == 'no' and light_state == 'ON':
    print("Turn Light OFF\n")
    light_state = 'OFF'
else:
    print("No change in light state.\n")

print(f"Light is {light_state}")
