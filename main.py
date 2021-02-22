from art import logo, vs
from game_data import data
import random
import os

print(logo)
end_of_game = False
score = 0
# print(len(data))


def generate_list_dictionary_A():
    dictionary_A = random.choice(data)
    # print(dictionary_A)
    return dictionary_A


def generate_list_dictionary_B():
    dictionary_B = random.choice(data)
    # print(dictionary_B)
    return dictionary_B


compare_A = generate_list_dictionary_A()
compare_B = generate_list_dictionary_B()
if compare_A == compare_B:
    compare_B = generate_list_dictionary_B


# print(compare_A["follower_count"])
# print(compare_B["follower_count"])

# While loop should start here.
while end_of_game == False:
    if compare_A == compare_B:
        compare_B = generate_list_dictionary_B()
    print(
        f"Campare A: {compare_A['name']}, a {compare_A['description']}, from {compare_A['country']}.")
    print(vs)
    print(
        f"Against B: {compare_B['name']}, a {compare_B['description']}, from {compare_B['country']} ")

    user_choice = input("Who has more followers? Type 'A' or 'B': ").casefold()

    dictionary_A_Followers = compare_A['follower_count']
    dictionary_B_Followers = compare_B['follower_count']
    if user_choice == 'a':
        user_take = dictionary_A_Followers
        if user_take > dictionary_B_Followers:
            score += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f"You're right! Current score: {score}.")
            compare_A = compare_B
        else:
            end_of_game = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")
    elif user_choice == 'b':
        user_take = dictionary_B_Followers
        if user_take > dictionary_A_Followers:
            score += 1
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f"You're right! Current score: {score}.")
            compare_A = compare_B
        else:
            end_of_game = True
            os.system('cls' if os.name == 'nt' else 'clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")

    if end_of_game == False:
        compare_B = generate_list_dictionary_B()
