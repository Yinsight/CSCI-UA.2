# function: swapcase
# input: string (string)
# processing: swap letters in string from lower case to upper case and vice versa
# output: a copy of the string in which letter cases are swapped
def swapcase(string):
    string_copy = ''

    for i in string:
        if 'a' <= i <= 'z':
            string_copy = string_copy + chr(ord(i) - 32)
        elif 'A' <= i <= 'Z':
            string_copy = string_copy + chr(ord(i) + 32)
        else:
            string_copy = string_copy + i

    return string_copy


def main():
    print(swapcase("Hello World"))
    print(swapcase("foobar"))
    print(swapcase("123 456 789"))
    print(swapcase(""))


if __name__ == '__main__':
    main()
