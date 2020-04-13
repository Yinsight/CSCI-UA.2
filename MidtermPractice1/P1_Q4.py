# function: calculate_discount
# input: num_of_tshirts (integer)
# processing: calculate the price based on number of t-shirts purchased
# output: returns the total price after applying discount
def calculate_discount(num_of_tshirts):
    num_of_tshirts = int(num_of_tshirts)
    original_cost = 20 * num_of_tshirts
    print("Original cost: $", "%.2f" % original_cost)

    if num_of_tshirts < 10:
        total_cost = original_cost
    elif num_of_tshirts < 20:
        total_cost = original_cost * (1 - 0.15)
    elif num_of_tshirts < 50:
        total_cost = original_cost * (1 - 0.25)
    elif num_of_tshirts < 100:
        total_cost = original_cost * (1 - 0.35)
    else:
        total_cost = original_cost * (1 - 0.45)

    print("Cost after discount: $", "%.2f" % total_cost)
    print("Thanks for your order!")
    return "%.2f" % total_cost


# function: purchase
# processing: validate input and call calculate_discount function
# output: print error message if input is not valid
def purchase():
    while True:
        num_of_tshirts = input("How many t-shirts would you like to purchase? ")
        if num_of_tshirts.isdigit():
            calculate_discount(num_of_tshirts)
            break
        else:
            print("Please enter a non-negative integer.")


def main():
    purchase()
    while True:
        choice = input("Would you like to purchase more t-shirts? (yes/no) ")
        if choice == "yes":
            purchase()
        elif choice == "no":
            break
        else:
            print("Please enter yes or no.")


if __name__ == '__main__':
    main()
