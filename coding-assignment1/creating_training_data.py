import random

OUTPUT_FILE = "training.txt"
NUM_ROUNDS = 100

# 0 = rock, 1 = paper, 2 = scissors
MOVE_MAP = {"rock": 0, "paper": 1, "scissors": 2}

wins = losses = ties = 0
training_data = []

for i in range(NUM_ROUNDS):
    print(f"\nRound {i+1} of {NUM_ROUNDS}")

    # user input
    while True:
        your_move_str = input("Your move (rock/paper/scissors): ").strip().lower()
        if your_move_str in MOVE_MAP:
            break
        print("Invalid input. Try again.")

    while True:
        cpu_move_str = input("Computer move (rock/paper/scissors): ").strip().lower()
        if cpu_move_str in MOVE_MAP:
            break
        print("Invalid input. Try again.")

    your_move = MOVE_MAP[your_move_str]
    cpu_move = MOVE_MAP[cpu_move_str]

    # determine score
    if your_move == cpu_move:
        score = 0
        ties += 1
    elif (your_move - cpu_move) % 3 == 1:
        score = 1
        wins += 1
    else:
        score = -1
        losses += 1

    training_data.append([cpu_move, your_move, score])

# save training data
with open(OUTPUT_FILE, "w") as f:
    for row in training_data:
        f.write(f"{row[0]} {row[1]} {row[2]}\n")

# success message to be displayed in the terminal
print("\nDone!")
print(f"Wins: {wins}, Losses: {losses}, Ties: {ties}")
print(f"Data saved to {OUTPUT_FILE}")

