# Thermostat agent.

temperature = int(input("Enter the temperature of the room:\n"))
if temperature < 20:
    print("Heater ON")
else:
    print("Heater OFF")