traffic = input("Enter the density of trafic 'High or Low':\n").strip().lower()

if traffic == 'high':
    print("Turn Green Light On.")
elif traffic == 'low':
    print("Turn Red Light On")
else:
    print("invalid input")

