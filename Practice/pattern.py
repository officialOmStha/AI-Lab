for i in range(1,6):
    print(i * "*")


rows = 5

for i in range(1, rows+1):
    print(" " * (rows -i), end="")
    print("* " * i, end="")
    print(" " * (rows-i))
