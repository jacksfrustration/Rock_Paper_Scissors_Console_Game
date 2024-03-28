import random

MOVES = ["Rock", "Paper", "Scissors"]

ASCII_MOVES = [
    """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
          _______
     ---'    ____)____
                ______)
               _______)
              _______)
     ---.__________)
""",
    """
             _______
         ---'   ____)____
                   ______)
                __________)
               (____)
         ---.__(___)
"""
]


def get_user_move():
    '''Loops until an appropriate move is input by the user and returns the value'''
    while True:
        user_move = input("What is your move? (Rock/Paper/Scissors)\n").title()
        if user_move in MOVES:
            return user_move
        else:
            print("Invalid move! Please choose Rock, Paper, or Scissors.")


def get_computer_move():
    '''generate and return the computer move'''
    return random.choice(MOVES)


def print_moves(user_move, computer_move):
    '''displays the moves both in text and ASCII art format'''
    user_index = MOVES.index(user_move)
    computer_index = MOVES.index(computer_move)
    print(f"\tYour move: {user_move}\n"
          f"{ASCII_MOVES[user_index]}\n"
          f"\tComputer Move: {computer_move}\n"
          f"{ASCII_MOVES[computer_index]}")


def determine_winner(user_move, computer_move):
    '''determines and returns winner based on the supplied moves'''
    if (user_move == "Rock" and computer_move == "Scissors") or \
            (user_move == "Scissors" and computer_move == "Paper") or \
            (user_move == "Paper" and computer_move == "Rock"):
        return "User"
    elif user_move == computer_move:
        return "Tie"
    else:
        return "Computer"


def main():
    '''main function for running the game'''
    user_score = 0
    computer_score = 0

    while True:
        start_playing = input("Start playing? (yes/no)\n").strip().lower()

        if start_playing == "no":
            break
        elif start_playing in ["yes", "y","ye"]:
            while True:
                user_move = get_user_move()
                computer_move = get_computer_move()

                print_moves(user_move, computer_move)

                winner = determine_winner(user_move, computer_move)
                if winner == "User":
                    user_score += 1
                    print("You win!!")
                elif winner == "Computer":
                    computer_score += 1
                    print("You lose!")
                else:
                    print("The match was tied!")

                print(f"User Score: {user_score}\n"
                      f"Computer Score: {computer_score}\n")

                keep_playing = input("Would you like to keep playing? (yes/no)\n").strip().lower()
                if keep_playing not in ["yes", "ye", "y"]:
                    break

            if user_score > computer_score:
                print("You won the game!")
            elif user_score < computer_score:
                print("The computer won the game!")
            else:
                print("The game ended in a tie!")

            print(f"Final scores:\nUser score: {user_score}\nComputer score: {computer_score}\n")
            break

        else:
            print(f"{start_playing} is not a valid option! Restarting the game.")


if __name__ == "__main__":
    main()