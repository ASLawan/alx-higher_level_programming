#!/usr/bin/python3

def best_score(a_dictionary):

    max = 0
    max_key = "key"
    if a_dictionary:
        for k, v in a_dictionary.items():
            if v > max:
                max = v
                max_key = k
    else:
        return None

    return max_key


if __name__ == "__main__":
    best_score(a_dictionary)
