#!/usr/bin/python3

def multiple_returns(sentence):

    if sentence == "":
        length = 0
        letter = "None"
    else:
        length = len(sentence)
        letter = sentence[0]
    return (length, letter)


if __name__ == "__main__":
    multiple_returns(sentence)
