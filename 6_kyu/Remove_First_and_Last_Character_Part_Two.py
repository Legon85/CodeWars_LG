def array(string):
    if len(string.split(',')) > 3:
        print(' '.join(string.split(',')[1:-1]))
    elif len(string.split(',')) == 3:
        print(string.split(',')[1])
    else:
        print(None)



array('1, 2, 3, 4, 5')