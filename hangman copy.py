
import random
from time import sleep


hangman_status = ['''
               +---+
               |   |
                   |
                   |
                   |
                   |
               =====
''',
'''
               +---+
               |   |
               o   |
                   |
                   |
                   |
               =====
''',
'''
               +---+
               |   |
               o   |
               |   |
                   |
                   |
               =====
''',
'''
               +---+
               |   |
               o   |
              /|   |
                   |
                   |
               =====
''',
'''
               +---+
               |   |
               o   |
              /|\  |
                   |
                   |
               =====
''',
'''
               +---+
               |   |
               o   |
              /|\  |
              /    |
                   |
               =====
''',
'''
               +---+
               |   |
               o   |
              /|\  |
              / \  |
                   |
               =====
''']

animal_names = []
food_names = []
plant_names = []

secret_word_list = []
blank_word_list = []
already_guessed = []

failed_guess_count = 0
answer = False
game_won = False


def convert_list_strings(list):
    converted_list = ""
    for letters in list:
        converted_list += letters

    return converted_list

def game_restart(game_status):
    if game_status == False:
        print("Game is restarting...")
        
        for seconds in range(3, 0, -1):
                print(seconds)
                sleep(1)

        game_intialization()

    new_game = input("Would you like to a new game? yes or no: ")
    if new_game == 'yes':
        game_intialization()
    else:
        exit()
    

def game_finished(score):
    global game_won

    if score == False:
        print('YOU LOST\n')
        
    else:
        print('YOU WON\n')
        game_won = True
    
    game_restart(score)

def state_of_man(guess_count):
    if guess_count == 6:
        print(hangman_status[guess_count])
        game_finished(False)
    return hangman_status[guess_count]


def verify_occurance(letter, word):

    if letter in already_guessed:
        print("\n\n\n\nYou have already guessed this")
    elif letter in blank_word_list:
        print("\n\n\n\nYou have already guessed this")
    elif letter not in already_guessed:
        pass
    else:
        return


def game_logic(letter, word):
    global failed_guess_count
    global answer

    if letter not in word:
        failed_guess_count += 1
        already_guessed.append(letter)
        print("\n\n\n\n\n\n\n\nIncorrect Answer.")

    if letter in word:
        for positions in range(len(word)):
            if letter == word[positions]:
                blank_word_list[positions] = letter
        
        print("\n\n\n\n\n\n\n\nCorrect Answer")

    game_play(word)


def game_play(word_list):
    global answer

    if '_' not in blank_word_list:
        game_finished(failed_guess_count)


    print("\n\n\n\n")


    print(state_of_man(failed_guess_count))
    print("Already Guessed: " + convert_list_strings(already_guessed))

    print("Hidden word: " + convert_list_strings(blank_word_list))
    letter_guessed = input("Pick a letter: ")

    if letter_guessed.isalpha():
        pass
    else:
        print("\n\n\n\nInput a alphabetical letter...")
        game_play(word_list)

    verify_occurance(letter_guessed, word_list)
    game_logic(letter_guessed, word_list)


def game_setup(secret_word):

    secret_word_list = list(secret_word.lower())

    for letters in range(len(secret_word)):
        if secret_word_list[letters] == ' ':
            blank_word_list.append(' ')

        blank_word_list.append('_')

    game_play(secret_word_list)
 
#Establishes a random word for the hangman
def game_intialization():

    global already_guessed
    global failed_guess_count
    global blank_word_list
    
    del already_guessed

    already_guessed = []
    blank_word_list = []

    failed_guess_count = 0

    print("\n\n\n\n\n\n\n")
    print("#####################################################")
    print("             WELCOME              TO                 ")
    print("                       ____                          ")
    print("|   |    /\    |\   | /      |\    /|    /\    |\   |")
    print("|___|   /  \   | \  | |   _  | \  / |   /  \   | \  |")
    print("|   |  /----\  |  \ | |    | |  \/  |  /----\  |  \ |")
    print("|   | /      \ |   \| \____/ |      | /      \ |   \|")
    print()
    print("#####################################################")

    print("\nCategories for word choice are animals, foods, and plants")
    user_category_choice = input("Type a category from the list above:")

    try:
        with open(f"{user_category_choice}.txt", "r") as item:
            lines = item.readlines()
    except:
        print("\nSorry that was not a valid answer please try again")
        print("Game is restarting...")
        #in case of invalid answer this executes
        for seconds in range(3, 0, -1):
            print(seconds)
            sleep(1)

        print()
        game_intialization()

    
    if user_category_choice == 'animals':
        for line in lines:
            animal_names.append(line.rstrip())

        secret_word = random.choice(animal_names)
        game_setup(secret_word)

    if user_category_choice == 'foods':
        for line in lines:
            food_names.append(line.rstrip())
       
        secret_word = random.choice(food_names)
        game_setup(secret_word)

    if user_category_choice == 'plants':
        for line in lines:
            plant_names.append(line.rstrip())

        secret_word = random.choice(plant_names)
        game_setup(secret_word)


game_intialization()    