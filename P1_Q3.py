# function: calculate_discount
# input: num_of_tshirts (integer)
# processing: calculate the price based on number of t-shirts purchased
# output: returns the total price after applying discount
def calculate_discount(num_of_tshirts):
    num_of_tshirts = int(num_of_tshirts)
    original_cost = 20 * num_of_tshirts

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
    return "%.2f" % total_cost


def main():
    print(calculate_discount(10))


if __name__ == '__main__':
    main()
