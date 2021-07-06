import random
import icons
import os

def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


def rock_paper_scissor():
    should_continue = True
    while should_continue:
        user_choice = int(input("Lets Play, Choose between the three, 0 For rock, 1 for paper, 2 for scissors \n"))
        if user_choice > 2 or user_choice < 0:
            print("Type a valid number to play")
        else:
            game_list = [icons.rock, icons.paper, icons.scissors]
            user_option = game_list[user_choice]
            print(user_option)
            computer_random = random.randint(0, 2)
            computer_option = game_list[computer_random]
            print("Computer Choose:")
            print(computer_option)
            if user_option == icons.rock and computer_option == icons.paper:
                print("You lost, Try again")
            elif user_option == icons.paper and computer_option == icons.scissors:
                print("You lost, Try again")
            elif user_option == icons.scissors and computer_option == icons.rock:
                print("You lost, Try again")
            elif user_option == computer_option:
                print("Draw, Try again")
            else:
                print("You won")
                should_continue = False


def caeser_cipher():
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    decoded_texts = ["gameover", "youwon", "winner"]
    word_to_decode = decoded_texts[random.randint(0, 2)]
    random_shift = random.randint(1, 3)
    end_text=""
    for letter in word_to_decode:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + random_shift
            end_text += alphabet[new_position]
    print(icons.logo)
    print(f"The Code is {end_text} \n")
    print("Decode this and you will be out of the room")
    answer_code = input("Write the decoded code here: \n").lower()
    if answer_code == word_to_decode:
        print("Congratulation, you won. Be happy you are one of the few who escaped the house")
    else:
        print("You lost, Don't worry to can try again anytime.")



print("This is the Darkest House you have ever seen!")
print(icons.house)

print("Once Entered it could be very difficult to come out.")
start_game = input("Do you want to Enter the House 'y' if you are brave enough and 'n' if you are scared :\n")

if start_game == 'y':
    print("Welcome to the room")
    print("Use your brains if you want to get out or be forever stuck here")
    print("You are in room no.1 to escape out you have to reach till room 3. Just use your brains")
    print("There are 4 gates in front of you 'red','blue','green','white'. The next room is the room of trust and "
          "only trust "
          "the trustworthy color.")
    room_one_answer = input("So choose wisely:").lower()
    if room_one_answer == "blue":
        print("Great you have choose the right room, lets move forward.")
        clear()
        print("Welcome to room 2")
        print("To Escape try to win Rock, Paper& Scissor")
        rock_paper_scissor()
        clear()
        print("Congratulation you have reached the end of the game just one step ahead and you will out!")
        print("But let me remind you this is the hardest part of the game. To escape the room you have to decode the "
              "Caeser Cipher. ")
        caeser_cipher()
        feedback=input("Enjoyed Playing :").lower()
        if feedback=="yes":
            print("I think your fear is over now, Enjoy")
        else:
            print("I Know you enjoyed playing but too shy to tell.")
    else:
        print("Sorry you are forever stuck in this room. The gate is filled with bricks.")



else:
    print("No problems try next time when you stop fearing!")
