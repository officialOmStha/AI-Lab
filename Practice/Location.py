# Class-Based Location Comparing
class Robot:
    def check_location(self, moves):
        # Count net horizontal and vertical moves
        horizontal = 0  # L = -1, R = +1
        vertical = 0    # U = +1, D = -1

        for move in moves:
            if move == "L":
                horizontal -= 1
            elif move == "R":
                horizontal += 1
            elif move == "U":
                vertical += 1
            elif move == "D":
                vertical -= 1

        # If net movement is zero, back to start
        return horizontal == 0 and vertical == 0


# Allowed moves
avi_moves = ["L", "R", "U", "D"]

# Input validation
inp_acc = False
while not inp_acc:
    inp = input("Enter the moves to be performed by the bot: \n").upper()
    if all(c in avi_moves for c in inp):
        inp_acc = True
    else:
        print("Invalid moves! Use only L, R, U, D.")

# Create robot object and check location
obj1 = Robot()
print("Back to start:", obj1.check_location(inp))