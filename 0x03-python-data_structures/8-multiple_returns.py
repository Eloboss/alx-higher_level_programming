#!/usr/bin/python3
def multiple_returns(sentence):
    boss = len(sentence)
    i = 0
    if boss == 0:
        return (boss, None)
    else:
        elo = boss, sentence[i]
        return elo
