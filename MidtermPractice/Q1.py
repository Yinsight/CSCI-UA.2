def build_a_computer(model, memory, drive):
    model = model.strip('"')

    model_price = {'Dell': 400, 'HP': 600}
    memory_price = {'4': 0, '8': 100, '16': 200}
    drive_price = {'256': 0, '512': 50, '1024': 100}

    cost = 0

    if str(model) in model_price.keys() and str(memory) in memory_price.keys() and str(drive) in drive_price.keys():
        cost = cost + model_price[str(model)] + memory_price[str(memory)] + drive_price[str(drive)]
        return cost
    else:
        return "Invalid Setup"


def main():
    print(build_a_computer("Dell", 4, 256))
    print(build_a_computer("HP", 4, 256))
    print(build_a_computer("Mac", 4, 256))
    print(build_a_computer("HP", 8, 256))
    print(build_a_computer("HP", 8, 512))
    print(build_a_computer("Dell", 4, 999))


if __name__ == '__main__':
    main()
