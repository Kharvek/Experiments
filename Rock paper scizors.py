import random

player_score = 0
computer_score = 0

while True:
    player_move = input("Choose [r]ock, [p]aper, [s]cissors or [q]uit: ")

    if player_move == "q":
        print("Game over!")
        break

    if player_move == "r":
        player_move = "rock"
    elif player_move == "p":
        player_move = "paper"
    elif player_move == "s":
        player_move = "scissors"
    else:
        print("Invalid input. Try again.")
        continue

    computer_move = random.choice(["rock", "paper", "scissors"])

    print(f"You chose: {player_move}")
    print(f"Computer chose: {computer_move}")

    if (player_move == "rock" and computer_move == "scissors") or \
       (player_move == "paper" and computer_move == "rock") or \
       (player_move == "scissors" and computer_move == "paper"):
        print("You win this round!")
        player_score += 1

    elif player_move == computer_move:
        print("This round is a draw!")

    else:
        print("You lose this round!")
        computer_score += 1

    print(f"Score → You: {player_score} | Computer: {computer_score}")
    print("-" * 30)
