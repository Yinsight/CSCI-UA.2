# function: checksum
# input: phrase (string)
# processing: calculate total ASCII value for a string
# output: returns the total ASCII value
def checksum(phrase):
    words = [i for j in phrase.split() for i in (j, ' ')][:-1]
    result = {}

    for word in words:
        current_sum = sum(map(ord, word))
        result[word] = current_sum

    total_sum = sum([result[word] for word in words])

    return total_sum


# function: validate
# processing: check if two strings have the same length and the same ASCII value
# output: print the result of validation
def validate():
    phrase1 = input("Enter phrase 1: ")
    phrase2 = input("Enter phrase 2: ")

    checksum_1 = checksum(phrase1)
    checksum_2 = checksum(phrase2)

    print("P1 has a length of {} and a checksum of {}".format(len(phrase1), checksum_1))
    print("P2 has a length of {} and a checksum of {}".format(len(phrase2), checksum_2))

    if len(phrase1) == len(phrase2) and checksum_1 == checksum_2:
        print("Passed!")
    else:
        print("Failed")


def main():
    validate()
    while True:
        option = input("Would you like to try again? ")
        if option == "Yes":
            validate()
        elif option == "No":
            break
        else:
            print("Please enter Yes or No.")


if __name__ == '__main__':
    main()
