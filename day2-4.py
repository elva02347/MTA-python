score_list = []
number = int(input('how many people?'))
for i in range(number):
    score = int(input('what\'s your score?'))
    if score<60:
        score = 60
        score_list.append(score)
    else:
        score_list.append(score)

print (score_list)
score_list.sort()
print('highest:', score_list[number -1])
print('lowest:', score_list[0])


