#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    counter = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            counter += 1
        except:
            continue
    print()
    return counter


my_list = [1, 2, 3, 4, 5]
safe_print_list_integers(my_list, 7)
