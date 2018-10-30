from random import randint

player = input("rock(r), paper(p), or scissors(s)\n:")

print(player, "vs", end=" ")

random_number = randint(1, 3)

if random_number == 1:
    computer = "r"
elif random_number == 2:
    computer = "p"
else:
    computer = "s"

print(computer)

if computer == player:
    print("DRAW!!")
elif computer == 'r' and player == 's':
    print("Computer wins")
elif computer == 's' and player == 'p':
    print("Computer wins")
elif computer == 'p' and player == 'r':
    print("Computer wins")
elif computer == 'p' and player == 's':
    print("Player wins")
elif computer == 'r' and player == 'p':
    print("Player wins")
elif computer == 's' and player == 'r':
    print("Player wins")

input("press any key to exit")
