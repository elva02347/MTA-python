import os
try:
    name = input('file in your file name:')
    e = os.path.isfile(name)
    f = open(name)
    print(f.readlines())
    f.close()
except:
    print('the file doesn\'t exist')
    