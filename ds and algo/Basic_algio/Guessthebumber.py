'''Guess the number
This notebook simulates a classic game where you have to guess a random number 
from within a certain range. Typically, you might have to guess a number from 
1 to 10, and have three guesses to get the right answer.

In this case, you'll need to guess a random number between 1 and 100, 
and you will 
have 7 tries.

Try running it and playing a round or two. Notice that the game always 
tells you whether your guess was too high or too low. This information allows you
 to rule out some of the numbers (so that you don't waste time guessing those 
 numbers).

With this fact in mind, try to make your guesses in the most efficient way you
 can. Specifically, try to make guesses that rule out the largest number of 
 possibilities each time.'''


import random

def  guess_the_number(total_tries, start_range, end_range):
    if start_range > end_range:
        start_range,end_range = end_range,start_range
    
    random_number = random.randint(start_range,end_range)
    
    success_message = "Awesome! You guessed correctly"
    failure_message = "Sorry! No more retries left"
    miss_message = "Oops! That's incorrect"


    num_tries = 0

    while num_tries<total_tries:
        attempt = int(input('Guess the number'))
        if attempt == random_number:
            print(success_message)
            return
        print(miss_message)
        if attempt<random_number:
            print('Go higher')
        
        else:
            print('go_lower')
        
        num_tries += 1

        print(failure_message)
    

