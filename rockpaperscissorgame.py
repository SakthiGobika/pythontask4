import string
import random
user_action=input("Enter a choice (rock,paper,scissors): ")
possible=["rock","paper","scissor"]
computer_action=random.choice(possible)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
if user_action==computer_action:
    print(f"It's a tie because of chhoosing {user_action}.\n")
elif user_action=="rock":
    if computer_action=="scissor":
        print(f"User won the match!By choosing {computer_action}.\n")
    else:
        print(f"User won the match!By choosing paper.\n")
elif user_action=="scissor":
    if computer_action=="rock":
        print(f"Computer won the match,By choosing {computer_action}.\n")
    else:
        print("Computer won the match by choosing paper.\n")
elif user_action=="paper":
    if computer_action=="scissor":
        print(f"Computer won the match by choosing {computer_action}.\n")
    else:
        print(f"Computer won the match by choosing rock.\n")
