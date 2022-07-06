"""
Rock, Paper, Scissors Game:
prompt a user to select either Rock,
Paper or Scissors while the computer will
randomly select one. Then compare the
choices and determine who the winner is. """

from random import randint
from time import sleep
options = [
  'ROCK',
  'PAPER',
  'SCISSORS'
]
message = {
  "tie": "Yawn it's a tie!",
  "won": "Yay you won!",
  "lost": "Aww you lost!"
}


def decide_winner(user_choice, computer_choice):
    """
    function takes a user input and a randomly
    generated computer choice and checks
    them against each other to determine
    a winning hand"""

    print(f"You have chosen {user_choice}")
    sleep(1)
    print(f"The computer has chosen {computer_choice}")
    sleep(1)
    if user_choice == computer_choice:
        print(message["tie"])
    elif user_choice == options[0] and computer_choice == options[2]:
        print(message["won"])
    elif user_choice == options[1] and computer_choice == options[0]:
        print(message["won"])
    elif user_choice == options[2] and computer_choice == options[1]:
        print(message["won"])
    else:
        print(message["lost"])


def play_RPS():
    """
    this fucntion runs the game, prompting the user for a
    selection and storing it in the user_choice variable
    """
    user_choice = input("Enter Rock, Paper or Scissors: ")
    user_choice = user_choice.upper()
    computer_choice = options[randint(0, 2)]
    decide_winner(user_choice, computer_choice)
    game = input("Would you like to play again?(y/n): ")
    game = game.upper()
    if game == 'Y':
        sleep(1)
        play_RPS()
    else:
        print("Bye Bye")


play_RPS()
