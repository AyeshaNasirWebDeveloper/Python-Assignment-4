def main():
    fruit_name = input("Enter a fruit: ")
    fruit_quantity = get_fruit_stock(fruit_name)
    
    if fruit_quantity > 0:
        print(f"This fruit is in stock! Here is how many: {fruit_quantity}")
    else:
        print("This fruit is not in stock.")

def get_fruit_stock(fruit):
    """
    Returns the number of fruit available in stock.
    """
    stock = {
        'apple': 2,
        'durian': 4,
        'pear': 1000
    }
    
    return stock.get(fruit, 0)

if __name__ == '__main__':
    main()
