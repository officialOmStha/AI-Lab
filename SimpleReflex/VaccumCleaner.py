# Vaccum cleaner agent

while True:
 status = input("Enter location status(Dirty/Clean): ").strip().lower()
 if status == "dirty":
    print("Action: Clean")
    break
 elif status == "clean":
    print("Action: Move")
    break
 else:
    print("Invalid input! Please enter only Dirty or Clean.")