t = 0
import random
ans = random.randint(1,100)
while True:
    guess = int(input('what\'s your guess?'))
    t = t+1
    if guess == ans :
        print('right!')
        print('you guess',t,'times~')
        break
    elif ans > guess:
        print('bigger!')
    else:
        print('smaller!')
    


