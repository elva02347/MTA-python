year = int(input('Which year?'))

if year%4 == 0:
    if year%400 == 0:
        print('lunar')
    elif year%100 == 0:
        print('common')
    else:
        print('lunar')
else:
    print('common')
