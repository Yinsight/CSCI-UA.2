def clean_sequence(sequence):
    valid_char = ['C', 'c', 'T', 't', 'A', 'a', 'G', 'g']
    cleaned_sequence = ''.join([char for char in sequence if char in valid_char])
    print("Good DNA Sequence:", cleaned_sequence.upper())

    valid_count = 0
    for char in sequence:
        if char in valid_char:
            valid_count = valid_count + 1

    invalid_count = len(sequence) - valid_count

    print("Valid nucleotides found:", valid_count)
    print("Invalid characters found:", invalid_count)


def main():
    sequence = input("Original DNA Sequence: ")
    clean_sequence(sequence)


if __name__ == '__main__':
    main()