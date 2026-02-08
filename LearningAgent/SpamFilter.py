# Learning Agent: Spam Filter

# Step 1 & 2: Initialize knowledge
spam_keywords = ["win", "free", "offer", "money"]

# Step 3: Learning loop
while True:
    # a. Read email content
    email = input("\nEnter email content: ").lower()

    # b. Predict spam or not spam
    prediction = "Not Spam"
    for word in spam_keywords:
        if word in email:
            prediction = "Spam"
            break

    # c. Display prediction
    print("Prediction:", prediction)

    # d. Ask user feedback
    feedback = input("Is the prediction correct? (yes/no): ").lower()

    # e. If correct → stop
    if feedback == "yes":
        print("\nPrediction confirmed. Learning complete.")
        break

    # f. Else → get new spam keyword
    elif feedback == "no":
        new_keyword = input("Enter a new spam keyword: ").lower()

        # g. Add keyword if not already known
        if new_keyword not in spam_keywords:
            spam_keywords.append(new_keyword)
            print("New keyword added to knowledge base.")
        else:
            print("Keyword already exists.")

        # h. Repeat prediction with updated knowledge
        print("Updating knowledge and re-evaluating...")

    else:
        print("Please enter yes or no.")

# Step 4: Stop
