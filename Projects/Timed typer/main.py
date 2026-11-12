import typer

print("Type the words and hit enter within the time limit!")

high_score = 0
player_wants_to_play = True
player_has_lost = False

while player_wants_to_play:
    # Play nine levels of a speed typing game.
    for level in range(1, 10):
        print("Level " + str(level))
        # Each level has four rounds.
        for round in range(1, 5):
            print("Round " + str(round))
            passed = typer.player_progression(level, round)
            if passed == 1:
                player_has_lost = True
                print("Oops! You have misspelled! Game over!")
                break
            elif passed == 2:
                player_has_lost = True
                print("Oops! You have ran out of time! Game over!")
                break
        if player_has_lost:
            break

    score = typer.get_score(level, round)
    if typer.is_high_score(score, high_score):
        print("New high score!")
    high_score = typer.get_high_score(score, high_score)
    print(f"You've played till level {level} round {round} and scored {score}.\nHighest Score is {high_score}.")
    play_again = input("Do you want to play again? (Y/n) ")
    if play_again == "Y":
        player_wants_to_play = True
    elif play_again == "n":
        player_wants_to_play = False
    else:
        print("Invalid response, only Y or n counts.")
        player_wants_to_play = False
print("Thanks for playing.")
