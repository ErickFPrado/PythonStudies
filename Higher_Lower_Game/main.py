import game_data
import art
import random
import os


# TODO: CHOOSE A RANDOM NUMBER [I];
# TODO: COMPARE A AGAINST B: "NAME, A ... , FROM ..." VERSUS ...
# TODO: WHO HAS MORE FOLLOWERS? TYPE "A" OR "B":
# TODO: WIN WHO HAS MORE FOLLOWERS


def get_random_data():
    return random.choice(game_data.data)


def data_format(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, followersA, followersB):
    if followersA > followersB:
        return guess == "a"
    else:
        return guess == "b"


def game():
    print(art.logo)
    score = 0
    game_continue = True
    accountA = get_random_data()
    accountB = get_random_data()

    while game_continue:
        accountA = accountB
        accountB = get_random_data()

        while accountA == accountB:
            accountB = get_random_data()

        print(f"Compare A: {data_format(accountA)}.")
        print(art.vs)
        print(f"Against B: {data_format(accountB)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = accountA["follower_count"]
        b_follower_count = accountB["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        os.system("cls")
        print(art.logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}")
        else:
            game_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")


game()
