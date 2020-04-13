def seat_cost(row_number, seat):
    row_number = int(row_number)
    cost = 0
    if 1 <= row_number <= 5:
        cost = cost + 500
    elif row_number == 10 or row_number == 11:
        cost = cost + 200
    elif row_number <= 25:
        cost = cost + 150
    else:
        return "invalid seat"

    if seat == 'B' or seat == 'E':
        cost = cost - 50
        return cost
    elif seat == 'A' or seat == 'C' or seat == 'D' or seat == 'F':
        return cost
    else:
        return "invalid seat"


def book_seat():
    total_cost = 0

    while True:
        row_number = input("Enter a row number (1-25): ")
        seat = input("Enter a seat (A, B, C, D, E or F): ")

        result = seat_cost(row_number, seat)

        if type(result) == str:
            print(result)
        else:
            print("This seat will cost", result)
            total_cost = total_cost + result
            print("Your total is currently", total_cost)

            choice = input("Would you like to buy another seat? ")
            if choice == "yes":
                pass
            elif choice == "no":
                print("The total cost for your flight will be:", total_cost)
                break
            else:
                print("Please enter yes or no.")
                break


def main():
    book_seat()


if __name__ == '__main__':
    main()