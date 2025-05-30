# game.py

# Inventory list to store collected items
inventory = []

def start_game():
    print("\nWelcome to the Adventure Game!")
    print("You wake up in a mysterious forest.")
    print("There is a path to the left and another to the right.")
    choice = input("Which way do you want to go? (left/right): ").lower()

    if choice == "left":
        left_path()
    elif choice == "right":
        right_path()
    else:
        print("Invalid choice. Try again.")
        start_game()

def left_path():
    print("\nYou walk along the left path and find a shiny sword on the ground.")
    print("Do you want to pick it up?")
    choice = input("(yes/no): ").lower()

    if choice == "yes":
        inventory.append("sword")
        print("You picked up the sword!")
    else:
        print("You left the sword behind.")

    print("You keep walking and reach a cave.")
    cave()

def right_path():
    print("\nYou take the right path and fall into a trap hole!")
    print("You have no way to escape.")
    game_over("You were trapped forever.")

def cave():
    print("\nInside the cave, a wild dragon appears!")
    if "sword" in inventory:
        print("You draw your sword and fight the dragon.")
        print("You defeat the dragon and find treasure behind it!")
        win_game()
    else:
        print("You have no weapon to fight the dragon.")
        game_over("The dragon defeats you.")

def game_over(reason):
    print("\nGame Over!")
    print(reason)
    play_again()

def win_game():
    print("\nCongratulations! You won the game!")
    print("You collected the treasure and escaped safely.")
    play_again()

def play_again():
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    if choice == "yes":
        inventory.clear()
        start_game()
    else:
        print("Thanks for playing!")

# Start the game
start_game()
