#!/usr/bin/python3
def remove_char_at(str, n):
    result = ""
    for i in range(0, len(str)):
        if i == n:
            continue
        result = result + str[i]
    return result
