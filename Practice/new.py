legal = ["A", "B", "C", "D"]
moves = "abcddcba"
l = False

if all(c in legal for c in moves.upper()):
    l = True

print(l)
if isinstance(l, bool):
    print("Hehe")
else:
    print("Boolean")