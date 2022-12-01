#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    elo = dir(hidden_4)
    for boss in elo:
        if boss[0:2] != "__":
            print(boss)
