file = open("text.txt", "r")
data = file.readlines()
spam = False
print(data)

spam_words = ["won", "click", "verify", "cheap", "interest"]

for word in data:
    for key in spam_words:
        if key in word.lower():
            spam = True
            break

if spam:
    print("File is a spam.")
else:
    print("File is geniun")

