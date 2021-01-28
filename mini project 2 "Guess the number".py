# "Guess the number" mini-project

import simplegui
import random

num_range = 100

# helper function to start and restart the game
def new_game():
    """ Creates a new game """
    global secret_number
    global num_range
    secret_number = random.randrange(1, num_range)
    print "New game. The range is [0, " + str(num_range) + ")"
    global no_guesses
    if num_range == 100:
        no_guesses = 7
    elif num_range == 1000:
        no_guesses = 10
    print "Number of remaining guesses is " + str(no_guesses)
    print " "
     
        
# define event handlers for control panel
def range100():
    """ Sets the range to [0, 100) """
    print "New game. The range is [0, 100)"
    global secret_number
    global num_range
    num_range = 100
    secret_number = random.randrange(1, num_range)
    global no_guesses
    no_guesses = 7
    print "Number of remaining guesses is " + str(no_guesses)
    print " "
                
      
def range1000():
    """ Sets the range to [0, 1000) """
    print "New game. The range is [0, 1000)"
    global secret_number
    global num_range
    num_range = 1000
    secret_number = random.randrange(1, num_range)
    global no_guesses
    no_guesses = 10
    print "Number of remaining guesses is " + str(no_guesses)
    print " " 
    
def input_guess(guess):
    """ Compares the input to the secret number """
    guess = int(guess)
    print "Guess was " + str(guess)
    global no_guesses
    no_guesses -= 1 
    if no_guesses > 0:
        print "Number of remaining guesses is " + str(no_guesses) 
        if guess < secret_number:
            print "Higher!"
            print " "
        elif guess > secret_number:
            print "Lower!"
            print " "
        else:
            print "Correct!"
            print " "
            new_game()
    elif no_guesses == 0:
        if guess == secret_number:
            print "Correct!"
            print " "
            new_game()
        else:
            print "You lost, try again"
            print " "
            new_game()

    
# create frame
frame = simplegui.create_frame ("Guess the number", 200, 200)
frame.add_button ("Run", new_game)
frame.add_button ("Range is [0, 100)", range100)
frame.add_button ("Range is [0, 1000)", range1000)


# register event handlers for control elements and start frame
frame.add_input("Enter your number", input_guess, 100)
frame.start()

