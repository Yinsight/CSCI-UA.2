# function: price_averaging
# # processing: ask user for number of product purchased and price of each product
# # output: return average cost of purchased products
def price_averaging():
    num_products = int(input("How many products did you purchase? "))
    total_cost = 0

    for i in range(num_products):
        while True:
            cost = round(float(input("How much did this product cost? ")), 2)
            if cost < 0:
                print("Sorry, only positive values allowed. Please try again.")
            else:
                total_cost = total_cost + cost
                break

    return total_cost / num_products


def main():
    print("Average Cost:",  "%.2f" % price_averaging())


if __name__ == '__main__':
    main()
