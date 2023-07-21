
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
                \n\n\n\n\n
''',
'''
               +---+
               |   |
               o   |
                   |
                   |
                   |
               =====
               \n\n\n\n\n
''',
'''
               +---+
               |   |
               o   |
               |   |
                   |
                   |
               =====
               \n\n\n\n\n
''',
'''
               +---+
               |   |
               o   |
              /|   |
                   |
                   |
               =====
               \n\n\n\n\n
''',
'''
               +---+
               |   |
               o   |
              /|\  |
                   |
                   |
               =====
               \n\n\n\n\n
''',
'''
               +---+
               |   |
               o   |
              /|\  |
              /    |
                   |
               =====
               \n\n\n\n\n
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

introduction_message = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    #####################################################
                WELCOME              TO                 
                            ____                          
    |   |    /\    |\   | /      |\    /|    /\    |\   |
    |___|   /  \   | \  | |   _  | \  / |   /  \   | \  |
    |   |  /----\  |  \ | |    | |  \/  |  /----\  |  \ |
    |   | /      \ |   \| \____/ |      | /      \ |   \|

    #####################################################
    \n\n\n\n\n\n\n\n'''


incorrect_answer = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
##################################################################
                         
                        INCORRECT ANSWER

##################################################################
\n\n\n\n\n'''

correct_answer = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
##################################################################
                         
                          CORRECT ANSWER

##################################################################
\n\n\n\n\n'''

repeated_answer = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
##################################################################
                         
              REPEATED ANSWER TRY A DIFFERENT LETTER

##################################################################
\n\n\n\n\n'''

winning_message = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
##################################################################
                         
                          YOU HAVE WON!!!

##################################################################
'''

losing_message = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
##################################################################
                         
                          YOU HAVE LOST...

##################################################################
'''



animal_names = []
food_names = []
plant_names = []

secret_word_list = []
blank_word_list = []
already_guessed = []

secret_word = ''
failed_guess_count = 0
game_won_count = 0
game_lost_count = 0


def game_stats():
    global secret_word
    return f'''
##################################################################
                         
                        GAME INFORMATION

                HIDDEN WORD IS: {secret_word}

                WIN TO LOSE RATIO IS: {str(game_won_count) + "/" + str(game_lost_count)}

##################################################################
'''


def convert_list_strings(list):
    converted_list = ""

    for letters in list:
        converted_list += letters

    return converted_list


def game_restart():

    new_game = input("Would you like to a new game? yes or no: ")
    if new_game == 'yes':
        game_intialization()
    else:
        exit()


def is_attempts_over(guess_count):
    global game_lost_count

    if guess_count == 6:
        game_lost_count += 1
        print(losing_message)
        print(game_stats())
        print(print_hangman_status(guess_count))
        game_restart()
    

def print_hangman_status(guess_count):
    return hangman_status[guess_count]
    

def is_letter_repeated(letter, word):
    if letter in already_guessed:
        return True
    else:
        return False
    

def is_letter_correct(letter, word):

    if letter in word:
        return True
    else:
        return False
    

def game_logic(letter, word):
    global failed_guess_count
    
    if is_letter_correct(letter, word) == True:

        if is_letter_repeated(letter, word) == True:
            print(repeated_answer)
        
        print(correct_answer)

        for positions in range(len(word)):
            if letter == word[positions]:
                blank_word_list[positions] = letter
                
    else:
        if is_letter_repeated(letter, word) == True:
            print(repeated_answer)

        else:
            failed_guess_count += 1
            already_guessed.append(letter)
            is_attempts_over(failed_guess_count)
            print(incorrect_answer)
    
    game_play(word)


def game_play(word_list):
    global game_won_count

    if '_' not in blank_word_list:
        print(winning_message)
        game_won_count += 1
        print(winning_message)
        print(game_stats())
        game_restart()

    print("\n\n\n\n")

    print(print_hangman_status(failed_guess_count))
    print("Already Guessed: " + convert_list_strings(already_guessed))

    print("Hidden word: " + convert_list_strings(blank_word_list))
    letter_guessed = input("Pick a letter: ")

    if letter_guessed.isalpha():
        pass
    else:
        print("\n\n\n\nInput a alphabetical letter...")
        game_play(word_list)

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
    global secret_word

    #This is only present because it fixed an issue I was having
    del already_guessed

    already_guessed = []
    blank_word_list = []

    failed_guess_count = 0

    print(introduction_message)

    print("\nCategories for word choice are animals, foods, and plants")
    user_category_choice = input("Type a category from the list above:")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

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
