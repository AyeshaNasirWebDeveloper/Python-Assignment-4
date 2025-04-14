def main():
    fruit_prices = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    total_amount = 0

    for fruit, price_per_unit in fruit_prices.items():
        quantity = int(input(f"How many ({fruit}) do you want to buy?: "))
        total_amount += price_per_unit * quantity

    print(f"\nYour total is ${total_amount}")

if __name__ == '__main__':
    main()
