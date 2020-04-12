def score_test(key, test):
    if len(key) != len(test):
        return "Too many or too few answers!"

    match = 0

    for i in range(len(key)):
        if key[i] == test[i]:
            match += 1
    return "Student earned {} out of {} possible points".format(match, len(key))


def main():
    key = "ab"
    test = "bc"
    print(score_test(key, test))


if __name__ == '__main__':
    main()
