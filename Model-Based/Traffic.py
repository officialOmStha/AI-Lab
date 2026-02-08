# Model Based Trqaffic light agent

light_state = "red" # internal memory
traffic = input("Traffic density (high/low): ").lower()

if traffic == "high" and light_state == "red":
    light_state = "green"
    print("Action: Change light to GREEN")
elif traffic == "low" and light_state == "green":
    light_state = "red"
    print("Action: Change light to RED")
else:
    print("Action: No change")
    
print("Current Light State:", light_state)
