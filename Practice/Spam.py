is_spam = False

spam_words = ["win", "help", "money"]

text = input("Enter the text: \n")

for word in spam_words:
    if word in text.lower():
        is_spam = True

if is_spam:
    print("The text is a spam.")
else:
    print("Text accepted.")


