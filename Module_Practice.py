import sys
import random

print('Guess my number! (0~10)')

num = random.randint(0,10)
tick = 0

while True:
    guess = int(sys.stdin.readline())
    tick = tick + 1

    if guess == num:
        print('You got it in %s tries!' % tick)
        break

    else:
        print('Guess again!')
    
        
                  
