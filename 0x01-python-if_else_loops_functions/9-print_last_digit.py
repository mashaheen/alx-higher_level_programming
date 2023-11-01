#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        x = number * -1
    else:
        x = number
    print('{:d}'.format(x % 10), end='')
    return x % 10
