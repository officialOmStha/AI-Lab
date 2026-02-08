# Learning Agent: Temperature Agent 

# Learning Agent: Temperature Agent

# Step 1 & 2: Initialize temperatures
hot_temp = 30
cold_temp = 18

# Step 3: Ask user preference
preference = input("Do you prefer hot or cold? ").strip().lower()

# Set initial temperature based on preference
if preference == "hot":
    current_temp = hot_temp
elif preference == "cold":
    current_temp = cold_temp
else:
    print("Invalid preference. Please restart.")
    exit()

# Step 4: Learning loop
while True:
    print(f"\nCurrent temperature: {current_temp}°C")
    comfortable = input("Are you comfortable? (yes/no): ").strip().lower()

    if comfortable == "yes":
        print("\nComfort achieved!")
        break
    elif comfortable == "no":
        if preference == "hot":
            current_temp += 1   # increase temperature
        else:
            current_temp -= 1   # decrease temperature
    else:
        print("Please answer with yes or no.")

# Step 5: Show final temperature
print(f"Final comfortable temperature: {current_temp}°C")

# Step 6: Stop
