import random
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

#logging.disable(logging.CRITICAL) #comment out this line to disable debug message
#logging.disable(logging.NOTEST) #comment out this line to enable debug message

guess = ''
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails:\n')
toss = random.randint(0, 1) # 0 is tails, 1 is heads

if toss == 0:
    toss = 'tails'
else:
    toss = 'heads'

logging.debug('toss : ' + toss)
logging.debug('guess : ' +  guess)

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = ''
    while guess not in ('heads', 'tails'):
        guess = input('Second Chance! Enter heads or tails:')
    logging.debug('second toss : ' + toss)
    logging.debug('second guess : ' + guess)
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')