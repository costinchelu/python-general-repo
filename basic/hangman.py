import os

def main():
    choice = True
    won = False
    game_over = False
    guessed = False
    countdown = 6
    secret = ""
    while choice:
        secret = input("Enter the word to be guessed by the other player:")
        decision = input("Are you happy with your choice? Press n for 'No' or y for 'Yes'")
        if decision.lower() != "n":
            choice = False
            print('\n' * 100)

    letters = list(secret.lower())
    result = []
    tried_letters = []
    for l in letters:
        result.append("_")

    while not game_over:
        print(result)
        player_input = input("Insert a letter:\n")
        if not tried_letters.__contains__(player_input):
            tried_letters.append(player_input)

            for it in range(len(letters)):
                if letters[it] == player_input:
                    result[it] = player_input
                    guessed = True
            if not guessed:
                countdown -= 1
                print(f"Wrong choice: {player_input}")
                print(f"You've got {countdown} tries left!")
            else:
                print(result)
            guessed = False

            if not result.__contains__("_"):
                game_over = True
                won = True

            if countdown == 0:
                game_over = True
        else:
            print("You already tried ", player_input)
    if won:
        print("YOU WON !!!")
    else:
        print("YOU LOST!")

if __name__ == '__main__':
    main()
