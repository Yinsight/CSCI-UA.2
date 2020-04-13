def summary():
    total_points = 0
    possible_points = 0

    for i in range(1, 11):
        while True:
            score = input("Score " + str(i) + " ")
            if float(score) <= 0:
                print("Sorry, " + score + " is not a valid score. Please try again.")
                continue
            else:
                total_points = total_points + float(score)
                possible_points = possible_points + 20
                break

    average_score = total_points/10

    print("Total points earned:", total_points)
    print("Total points possible:", possible_points)
    print("Average homework score:", str(average_score) + " / 20.0")


def main():
    summary()


if __name__ == '__main__':
    main()