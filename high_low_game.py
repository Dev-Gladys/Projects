import random
from data_high_low_game import data
from high_low_art import vs, logo
account_b = random.choice(data)
score = 0


def access_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name} is a {description} from {country}"

#Check answers

def check_answer(guess, followers_a, followers_b):
    if followers_a > followers_b:
        return guess == "a"
    else:
        return guess == "b"


game_on = True

while game_on:
    print("WELCOME TO THE GAME:")
    print(logo)

    #get random data and ensure that same question does not repeat for a and b in a section
    account_a = account_b

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {access_data(account_a)}")
    print(vs)
    print(f"Compare B: {access_data(account_b)}")

    guess = input("Who has the highest followers on IG? A or B: ").lower()

    #Access followers' count from data
    followers_a=account_a['follower_count']
    followers_b=account_a['follower_count']

    answer = check_answer(guess, followers_a, followers_b)

    #Check answer if correct player get 1 point and if false, asked to playagain and shown score
    if answer:
        score += 1
        print(f"Correct! Your current score is {score}")
    else:
        print(f"incorrect your current score is {score}")
        play_again = input("Do you want to play again? Yes or No: ").lower()
        if play_again == "no":
            game_on = False
            print(f"Bye! Your final score is {score}")

