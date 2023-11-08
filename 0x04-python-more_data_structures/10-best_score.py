#!/usr/bin/python3
def best_score(a_dictionary):
    if (len(list(a_dictionary)) == 0):
        return None
    score = 0
    lead = ''
    for x, y in a_dictionary.items():
        if y > score:
            score = y
            lead = x
    return lead
