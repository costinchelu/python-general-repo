import random

def main():
    moves = "✊", "✋", "✌"

    user_choice = 100
    computer_choice = random.randint(0, 2)

    check = True
    while check:
        choose = input(
    '''
    Choose:
    0 for rock ✊
    1 for paper ✋
    2 for scissor ✌
    ''')
        if choose == "0":
            user_choice = 0
            check = False
        elif choose == "1":
            user_choice = 1
            check = False
        elif choose == "2":
            user_choice = 2
            check = False
        else:
            print("Wrong choice! 😌 Try again.")

    print(f"\nYou play: {moves[user_choice]}\nComputer plays: {moves[computer_choice]}\n")

    result = user_choice - computer_choice
    if result == 0:
        print("Equal match! 🫠")
    elif result == -1 or result == 2:
        print("You lost! 😭")
    else:
        print("You won! 😁")

if __name__ == "__main__":
    main()