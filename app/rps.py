# the "app/rps.py" file (v1)...

#
# USER SELECTION
#

u = input("Please choose one of 'Rock', 'Paper', or 'Scissors': ").lower()
print("USER CHOICE:", u)
if u not in ["rock", "paper", "scissors"]:
    print("OOPS, TRY AGAIN")
    exit()

#
# COMPUTER SELECTION
#

from random import choice

c = choice(["rock", "paper", "scissors"])
print("COMPUTER CHOICE:", c)

#
# DETERMINATION OF WINNER
#

if u == "rock" and c == "rock":
    print("TIE GAME")
elif u == "rock" and c == "paper":
    print("COMPUTER WINS")
elif u == "rock" and c == "scissors":
    print("USER WINS")
elif u == "paper" and c == "rock":
    print("COMPUTER WINS") # OOPS
elif u == "paper" and c == "paper":
    print("TIE GAME")
elif u == "paper" and c == "scissors":
    print("USER WINS") # OOPS
elif u == "scissors" and c == "rock":
    print("COMPUTER WINS")
elif u == "scissors" and c == "paper":
    print("USER WINS")
elif u == "scissors" and c == "scissors":
    print("TIE GAME")