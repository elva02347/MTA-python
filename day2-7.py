import random
while True:
    inkey = input('按a再按enter開始~，按enter結束!')
    if len(inkey) > 0 :
        num  = random.randint(1,6)
        print('your point:',str(num))
    else:
        print('game over')
        break
        