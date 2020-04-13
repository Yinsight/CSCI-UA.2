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


def main():
    print("20 A: ", seat_cost(20, 'A'))
    print("25 B: ", seat_cost(25, 'B'))
    print("10 A: ", seat_cost(10, 'A'))
    print("11 B: ", seat_cost(11, 'B'))
    print("1 A: ", seat_cost(1, 'A'))
    print("2 B: ", seat_cost(2, 'B'))
    print("25 Q: ", seat_cost(25, 'Q'))
    print("99 A: ", seat_cost(99, 'A'))
    print("85 X: ", seat_cost(85, 'X'))


if __name__ == '__main__':
    main()




