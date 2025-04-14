MAX_FIB_VALUE = 10000

def main():
    first_term = 0  # Fib(0)
    second_term = 1  # Fib(1)

    while first_term <= MAX_FIB_VALUE:
        print(first_term)
        
        next_term = first_term + second_term
        
        first_term = second_term
        second_term = next_term

# Run the program
if __name__ == '__main__':
    main()
