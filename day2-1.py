for i in range(100):
    if ((i + 1) % 3) == 0:
        continue
    elif ((i + 1) % 5) == 0:
        continue
    else:
        print(i+1)
    