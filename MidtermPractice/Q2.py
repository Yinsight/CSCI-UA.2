def build_a_computer(model, memory, drive):
    model = model.strip('"')

    model_price = {'Dell': 400, 'HP': 600}
    memory_price = {'4': 0, '8': 100, '16': 200}
    drive_price = {'256': 0, '512': 50, '1024': 100}

    global cost
    cost = 0

    if str(model) in model_price.keys() and str(memory) in memory_price.keys() and str(drive) in drive_price.keys():
        cost = cost + model_price[str(model)] + memory_price[str(memory)] + drive_price[str(drive)]
        return cost
    else:
        return "Invalid Setup"


def check_cost():
    print("Your shopping cart is currently:", total_cost, "dollars")
    model = input("Enter a model (Dell or HP): ")
    memory = input("How much memory do you want? (4, 8, 16): ")
    drive = input("Hard drive size? (256, 512, 1024): ")
    cost = build_a_computer(model, memory, drive)
    if type(cost) == str:
        print("We're sorry, but that setup is not available. Please try again.")
    else:
        print("Your setup will cost: ", cost)
    return cost


def main():
    global total_cost
    total_cost = 0
    check_cost()
    total_cost = total_cost + cost
    while True:
        option = input("Would you like to price another computer? ")
        if option == "yes":
            check_cost()
            total_cost = total_cost + cost
        elif option == "no":
            print("Your total shopping cart is:", total_cost, "dollars")
            break
        else:
            print("Please enter yes or no in lower case.")


if __name__ == '__main__':
    main()
