print("You're in a soccer game.")
name = input("Melvin")
print("A defender is pressing Melvin")

move = input("turn")
if move == "turn":
    print("Melvin turns and dribbles into space.")
elif move == "pass":
    print("Melvin passes to a teammate with more space.")
else:
    print("Melvin hesitates and the defender takes the ball!")

next_move = input("dribble")
if next_move == "dribble":
    print("Melvin nutmegs the last defender and is through on goal!")
elif next_move == "cross":
    print("Melvin crosses to the striker beside him and he is through on goal!")
else:
    print(
        "Melvin gets tackled by the last defender and the opposition go on a counter attack."
    )

final_move = input("shoot")
if final_move == "shoot":
    print("Melvin shoots in the top corner and scores!")
else:
    print("Melvin shoots but the goalkeeper saves it.")
