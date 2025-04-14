def find_average(num1: float, num2: float):
    return (num1 + num2) / 2

def main():
    average_one = find_average(0, 10)
    
    average_two = find_average(8, 10)
    
    final_average = find_average(average_one, average_two)
    
    print("First Average:", average_one)
    print("Second Average:", average_two)
    print("Final Average:", final_average)

if __name__ == '__main__':
    main()
