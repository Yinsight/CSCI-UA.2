# function: compute_roll
# input: rolls (string)
# processing: convert input string to a list of integers
# output: print the number of elements in the string, the total value of elements, and their average value
def compute_roll(rolls):
    elements = rolls.split(",")
    values = []
    for e in elements:
        values.append(int(e))

    print("Total # of rolls:", len(values))
    print("Total value of all rolls:", sum(values))
    print("Average roll:", sum(values)/len(values))


def main():
    compute_roll("1,5,2,3,5,4,4,3,1,1,1,2,3,1,5,6,2")


if __name__ == '__main__':
    main()

