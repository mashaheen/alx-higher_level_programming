#!/usr/bin/python3
def uppercase(str):
    for c in str:
        x = ord(c)
        if x >= 97 and x <= 122:
            print('{:c}'.format(x-32), end='')
            continue
        print('{:c}'.format(x), end='')
    print()
